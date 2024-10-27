from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from robot.domain.services.IMPSecuenciaMovimientosService import SecuenciaMovimientoService

# Crear el servicio del robot
sec_serv = SecuenciaMovimientoService()


@csrf_exempt
def crear_secuencia(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)  # Convertir el cuerpo de la solicitud a un diccionario Python

            datos = [body["titulo"],
                     body["tipo"],
                     body["movimientos"]
            ]
            
            # crear la secuencia
            respuesta = sec_serv.create_secuencia(datos[0], datos[1], datos[2])

            # Si no ha habido errores, se mandará la respuesta
            if respuesta != () and respuesta != None:


                return JsonResponse({"respuesta": respuesta}) #retornar el respuesta
            else:
                return JsonResponse({"error": "Failed to create sequence."}, status=400)
        except Exception as e:
            print("error2")
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponse(status=405)  # Método no permitido


def get_all_secuencias(request):

    if request.method == "GET":
    
        try:
            secuencias = sec_serv.get_all_secuencias()
            return JsonResponse({"secuencias": secuencias})
        except Exception as e:
            print("errorxd")
            return JsonResponse({"error": str(e)}, status=500)
        
    else:
        return HttpResponse(status=405)  # Método no permitido
    

@csrf_exempt
def delete_secuencia(request):
    if request.method == "DELETE":
        try:
            id_sec = request.GET.get("id")
            respuesta = sec_serv.delete_secuencia(id_sec)

            return JsonResponse({"respuesta": respuesta})
        except Exception as e:
            print("errorxd")
            return JsonResponse({"error": str(e)}, status=500)
        
    else:
        return HttpResponse(status=405)  # Método no permitido
    
@csrf_exempt
def get_secuencia(request):
    if request.method == "GET":
        try:
            id_sec = request.GET.get("id")
            secuencias = sec_serv.get_secuencia(id_sec)

            return JsonResponse({"secuencia": secuencias})
        except Exception as e:
            print("errorxd")
            return JsonResponse({"error": str(e)}, status=500)
    
    else:
        return HttpResponse(status=405)  # Método no permitido
    