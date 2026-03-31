# Python script para completar el index.html

script_final = '''
    // Animations on Scroll
    const animateElements = document.querySelectorAll('.animate-on-scroll');

    const animateOnScroll = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animated');
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    animateElements.forEach(el => animateOnScroll.observe(el));

    // Form Validation
    const contactForm = document.getElementById('contactForm');
    const formSuccess = document.getElementById('formSuccess');

    if (contactForm) {
      contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        let isValid = true;
        const requiredFields = ['nombre', 'email', 'telefono', 'mensaje'];
        
        requiredFields.forEach(field => {
          const input = document.getElementById(field);
          const formGroup = input.closest('.form-group');
          
          if (!input.value.trim()) {
            formGroup.classList.add('error');
            isValid = false;
          } else {
            formGroup.classList.remove('error');
            
            // Email validation
            if (field === 'email') {
              const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
              if (!emailRegex.test(input.value)) {
                formGroup.classList.add('error');
                isValid = false;
              }
            }
          }
        });
        
        if (isValid) {
          // Simular envío exitoso
          formSuccess.classList.add('show');
          contactForm.reset();
          
          // Track conversion
          if (typeof gtag !== 'undefined') {
            gtag('event', 'form_submit', {
              event_category: 'conversion',
              event_label: 'contact_form',
              value: 1
            });
          }
          
          setTimeout(() => {
            formSuccess.classList.remove('show');
          }, 5000);
        }
      });
      
      // Remove error on input
      document.querySelectorAll('.form-group input, .form-group textarea').forEach(input => {
        input.addEventListener('input', function() {
          this.closest('.form-group').classList.remove('error');
        });
      });
    }

    // Register Service Worker (PWA)
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
          .then(registration => {
            console.log('SW registered:', registration.scope);
          })
          .catch(error => {
            console.log('SW registration failed:', error);
          });
      });
    }
  </script>
</body>
</html>
'''

# Leer el archivo actual
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Verificar si ya está completo
if '</script>\n</body>\n</html>' in content:
    print("✓ El archivo ya está completo")
else:
    # Agregar el script final
    # Buscar donde cortar (si se cortó en medio del script)
    if 'const animateOnScroll' in content:
        # Ya tiene parte del script, agregar el resto
        cut_index = content.find('const animateOnScroll')
        content = content[:cut_index] + script_final
    else:
        # Agregar al final antes de </body>
        content = content.replace('</body>', script_final + '</body>')
    
    # Guardar
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Archivo completado exitosamente")
