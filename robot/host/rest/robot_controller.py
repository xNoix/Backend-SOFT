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
def move_robot_joints(request):
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

            # Si no ha habido errores, se mandará la respuesta
            if current_pos != [] and current_pos != None:
                pos_joints = {'j1': current_pos[0][0],
                            'j2': current_pos[0][1],
                            'j3': current_pos[0][2],
                            'j4': current_pos[0][3],
                            'j5': current_pos[0][4],
                            'j6': current_pos[0][5]}
                pos_pose = {'p1': current_pos[1][0],
                            'p2': current_pos[1][1],
                            'p3': current_pos[1][2],
                            'p4': current_pos[1][3],
                            'p5': current_pos[1][4],
                            'p6': current_pos[1][5]}
                cur_pos = {'current_joints': pos_joints,
                        'current_pose': pos_pose}

            
                return JsonResponse(cur_pos) #retornar el current_pos
            else:
                return JsonResponse({"error": "Failed to move the robot"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponse(status=405)  # Método no permitido


@csrf_exempt  # Django requiere protección CSRF para solicitudes POST; puedes deshabilitarlo para probar.
def move_robot_pose(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)  # Convertir el cuerpo de la solicitud a un diccionario Python
            
            # Crear una lista con los valores de las articulaciones
            pose_positions = [
                body["pose_1"],
                body["pose_2"],
                body["pose_3"],
                body["pose_4"],
                body["pose_5"],
                body["pose_6"]
            ]
            
            # Llamar al método con la lista de radianes
            current_pos = robot_service.move_pose(pose_positions)

            # Si no ha habido errores, se mandará la respuesta
            if current_pos != [] and current_pos != None:
                pos_joints = {'j1': current_pos[0][0],
                            'j2': current_pos[0][1],
                            'j3': current_pos[0][2],
                            'j4': current_pos[0][3],
                            'j5': current_pos[0][4],
                            'j6': current_pos[0][5]}
                pos_pose = {'p1': current_pos[1][0],
                            'p2': current_pos[1][1],
                            'p3': current_pos[1][2],
                            'p4': current_pos[1][3],
                            'p5': current_pos[1][4],
                            'p6': current_pos[1][5]}
                cur_pos = {'current_joints': pos_joints,
                        'current_pose': pos_pose}

            
                return JsonResponse(cur_pos) #retornar el current_pos
            else:
                return JsonResponse({"error": "Failed to move the robot"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponse(status=405)  # Método no permitido