from django.http.response import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile

import base64
import json
import io, os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class EcryptDecryptMiddleware:

    def is_ajax(self, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    
    def _get_iv(self):
        return 'BBBBBBBBBBBBBBBB'.encode('utf-8')
    
    def _get_key(self):
        return b'Sixteen byte key'
    
    def _decrypt_file_inst(self, request, enc_file):
        # Assume 'blob' is the Blob object obtained from your AJAX call
        blob_data = enc_file.read()

        cipher = AES.new(self._get_key(), AES.MODE_CBC, self._get_iv())
        enc = base64.b64decode(blob_data)
        pt = unpad(cipher.decrypt(enc), AES.block_size)

        # Create an in-memory file object and write the decrypted data to it
        memory_file = io.BytesIO()
        memory_file.write(pt)
        memory_file.seek(0)

        # Create an InMemoryUploadedFile object from the in-memory file object
        decoded_file = InMemoryUploadedFile(memory_file, None, enc_file.name, enc_file.content_type, len(pt), None)

        # Add the InMemoryUploadedFile object to the request.FILES dictionary
        request.FILES['file_path'] = decoded_file

    def _decrypt_request(self, request):
        enc = getattr(request, request.method, {}).get("data", {})
        enc_file = request.FILES.get("encrypted_file", None)
        if isinstance(enc, dict) and len(enc.keys()) == 0:
            return
        
        if enc_file:
            self._decrypt_file_inst(request, enc_file)
        enc = base64.b64decode(enc)
        cipher = AES.new(self._get_key(), AES.MODE_CBC, self._get_iv())
        pt = unpad(cipher.decrypt(enc), 16)
        setattr(request, getattr(request, "method", "POST"), json.loads(pt))

    def _encrypt_response(self, response):
        data= pad(response.content, 16)
        cipher = AES.new(self._get_key(), AES.MODE_CBC, self._get_iv())
        enc_data = base64.b64encode(cipher.encrypt(data))
        return JsonResponse({"data": enc_data.decode("utf")}, status=response.status_code)
    
    def __call__(self, request):

        if(self.is_ajax(request)):
            self._decrypt_request(request)
        
        response = self.get_response(request)

        if(self.is_ajax(request)):
            return self._encrypt_response(response)

        return response
