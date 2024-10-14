from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from robot.domain.services.IMProbotService import RobotService_imp  # El servicio del robot
from robot.domain.services.IMProbotConnection import RobotConnectionIP  # El servicio del robot

# Crear el servicio del robot
robot_service = RobotService_imp(RobotConnectionIP())


# Vista para obtener la informacion de conexión del robot
def get_robot_connection_info(request):
    try:
        connection_info = robot_service.get_connection_info()
        return JsonResponse({
            "ip": connection_info["ip"],
            "port": connection_info["port"]
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
# Para obtener acceso al robot si esta libre
def get_robot_access(request):
    print("Acceso al robot obtenido.")
    
    """Para obtener acceso al robot solo si esta liberado.
        Si ya esta en uso, no dar acceso.
        Esto permite el acceso a llamar a las funciones de control del robot"""
    
    """El metodo de consulta es por base de datos, no deberia iniciarse el servicio del robot ni nada relacionado
        a este sin antes haber obtenido acceso."""
    
    

# Vista para mover el robot
"""SOLO SI SE TIENE ACCESO AL ROBOT
EN UN PRINCIPIO NO DEBERIA PODER LLAMARSE A ESTAS VISTAS SI NO SE HA CONCEDIDO ACCESO"""
@csrf_exempt  # Django requiere protección CSRF para solicitudes POST; puedes deshabilitarlo para probar.
def move_robot(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)  # Convertir el cuerpo de la solicitud a un diccionario Python
            
            # Crear una lista con los valores de las articulaciones
            joint_positions = [
                body["joint_1"],
                body["joint_2"],
                body["joint_3"],
                body["joint_4"],
                body["joint_5"],
                body["joint_6"]
            ]
            
            # Llamar al método con la lista de radianes
            current_pos = robot_service.move_joints(joint_positions)

            if current_pos != []:
                return JsonResponse({"message": "Robot moved successfully"}) #retornar el current_pos
            else:
                return JsonResponse({"error": "Failed to move the robot"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponse(status=405)  # Método no permitido
    
robot_service.move_joints(['1','2','3','4','5','6'])