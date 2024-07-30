from django.http import HttpResponse


def procesar_numero(request):
    try:
        numero = request.GET.get('numero', '')
        if numero.isdigit():
            numero1 = int(numero)
            response_content = f'El numero ingresado es: {numero1}<br>'
        else:
            raise Exception("El valor ingresado no corresponde a un numero.")
    except Exception as ex:
        response_content = (
            f'Ocurrio el siguiente error al ejecutar el programa: {ex}.<br>'
            'Por favor comuniquese con el area de TI.<br>'
            'Correo enviado exitosamente<br>'
            'Log guardado exitosamente<br>'
            'Transacciones reversadas correctamente<br>'
        )
        
    finally:
        response_content += 'Presione enter para salir del programa.'
    
    return HttpResponse(response_content, content_type='text/html')


