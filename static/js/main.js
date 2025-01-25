/**
* Template Name: NiceAdmin - v2.5.0
* Template URL: https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    if (all) {
      select(el, all).forEach(e => e.addEventListener(type, listener))
    } else {
      select(el, all).addEventListener(type, listener)
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Sidebar toggle
   */
  if (select('.toggle-sidebar-btn')) {
    on('click', '.toggle-sidebar-btn', function (e) {
      select('body').classList.toggle('toggle-sidebar')
    })
  }

  /**
   * Search bar toggle
   */
  if (select('.search-bar-toggle')) {
    on('click', '.search-bar-toggle', function (e) {
      select('.search-bar').classList.toggle('search-bar-show')
    })
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Initiate tooltips
   */
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  })

  /**
   * Initiate quill editors
   */
  // $.each( $(".quill-editor-default"), function( key, value ) {
  //   quill = new Quill(value, {
  //       theme: 'snow',
  //       placeholder: 'Enter the content here',
  //     });
  // });

  if (select('.quill-editor-default')) {
    $.each($(".quill-editor-default"), function (key, value) {
      var quill = new Quill(value, {
        theme: 'snow',
        placeholder: 'Enter the content here',
      });
      quill.on("text-change", handleQuillTextChange.bind(quill));
    });
  }


  if (select('.quill-editor-bubble')) {
    new Quill('.quill-editor-bubble', {
      theme: 'bubble'
    });
  }

  if (select('.quill-editor-full')) {
    new Quill(".quill-editor-full", {
      modules: {
        toolbar: [
          [{
            font: []
          }, {
            size: []
          }],
          ["bold", "italic", "underline", "strike"],
          [{
            color: []
          },
          {
            background: []
          }
          ],
          [{
            script: "super"
          },
          {
            script: "sub"
          }
          ],
          [{
            list: "ordered"
          },
          {
            list: "bullet"
          },
          {
            indent: "-1"
          },
          {
            indent: "+1"
          }
          ],
          ["direction", {
            align: []
          }],
          ["link", "image", "video"],
          ["clean"]
        ]
      },
      theme: "snow"
    });
  }


  /**
   * Initiate Bootstrap validation check
   */
  var needsValidation = document.querySelectorAll('.needs-validation')

  Array.prototype.slice.call(needsValidation)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('form-validated')
      }, false)
    })

  /**
   * Initiate Datatables
   */
  const datatables = select('.datatable', true)
  datatables.forEach(datatable => {
    $(datatable).DataTable({
      responsive: true,
      columnDefs: [
        { targets: '_all', className: 'dt-center' }
      ]
    });
  })

  /**
   * Autoresize echart charts
   */
  const mainContainer = select('#main');
  if (mainContainer) {
    setTimeout(() => {
      new ResizeObserver(function () {
        select('.echart', true).forEach(getEchart => {
          echarts.getInstanceByDom(getEchart).resize();
        })
      }).observe(mainContainer);
    }, 200);
  }

})();


/**
   * method to handle show date and time picker
   */
$(document).on("click", "input[type=date]", function (e) { this.showPicker(); })
$(document).on("click", "input[type=time]", function (e) { this.showPicker(); })
$(document).on("click", "input[type=datetime-local]", function (e) { this.showPicker(); })


/**
   * method to handle button hide on every submit
   */
function hideSubmitButton(form_id) {
  var form_button = $("#" + form_id).find("[type='submit']").hide();
  var new_button = $("#bootstrap-loader");
  new_button.show();
  $(form_button).replaceWith(new_button).show();

  return form_button
}

function hideSubmitButtonOnModal(form_id) {
  
  // var form_button = $("#" + form_id).parents.find("button[id='input-modal-confirmation']").prevObject;
  var form_button = $(".modal-footer").find("button[id='input-modal-confirmation']");
  form_button.hide()
  form_button.prop('disabled', true);
  var new_button = $("#bootstrap-loader");
  new_button.show();
  $(form_button).replaceWith(new_button).show();

  return form_button
}


function showSubmitButton(button) {
  // $("#"+form_id).find("[type='submit']").show();
  $("#bootstrap-loader").after(button.show());
  $("#bootstrap-loader").hide()
}


function hideAnyElement(element_id) {
  $("#" + element_id).hide();
}


function showAnyElement(element_id) {
  $("#" + element_id).show();
}


function auto_grow(element) {
  element.style.height = "200px";
  element.style.height = (element.scrollHeight) + "px";
}


function handleQuillTextChange() {
  const input_field_id = $(this.root).parents(".quill-editor-default").data("input-field-id");

  var quill_hidden_input = $("#" + input_field_id);
  if (this.getText() == "\n") {
    quill_hidden_input.val(""); // Setting empty value
  }
  else {
    quill_hidden_input.val(this.root.innerHTML.replace(/\s+/g, ' ').trim()); // quill instance was binded to function during registration
  }
}
