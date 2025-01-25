function ReturnEncryptionDecryptionPassword() {
    return CryptoJS.enc.Utf8.parse("Sixteen byte key");
};

function ReturnEncryptionDecryptionIV() {
    return CryptoJS.enc.Utf8.parse(ReturnEncryptionDecryptionIVKey)
};

function CustomEncrypt(dataToEncrypt) {
    var encrypted = CryptoJS.AES.encrypt(JSON.stringify(dataToEncrypt), ReturnEncryptionDecryptionPassword(), { iv: ReturnEncryptionDecryptionIV(), mode: CryptoJS.mode.CBC});
    return encrypted.toString();
}

function readFile(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        let arrayBuffer;
        try {
            reader.onload = function(e) {
                resolve(e.target.result);
            };
            reader.readAsArrayBuffer(file);
        } catch (error) {
            reject(error)
        }
    })
}

async function CustomEncryptFileObject(file_to_encrypt) {

    let result = await readFile(file_to_encrypt);
    var word_array_crypto_obj = CryptoJS.lib.WordArray.create(new Uint8Array(result));
    const encrypted = CryptoJS.AES.encrypt(
        word_array_crypto_obj,
        ReturnEncryptionDecryptionPassword(),
        {
            iv: ReturnEncryptionDecryptionIV(),
            mode: CryptoJS.mode.CBC
        }
    );
    const encryptedArrayBuffer = encrypted.toString();
    const encryptedFile = new Blob([encryptedArrayBuffer], { type: 'application/octet-stream' });
    return encryptedFile;
}

function CustomDecrypt(encryptedString) {
    var decrypted =  CryptoJS.AES.decrypt(encryptedString, ReturnEncryptionDecryptionPassword(), { iv: ReturnEncryptionDecryptionIV(), mode: CryptoJS.mode.CBC});
    return JSON.parse(decrypted.toString(CryptoJS.enc.Utf8));
}