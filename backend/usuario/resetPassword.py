import pytz
from datetime import datetime
from rest_framework.response import Response
import secrets
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.core.mail import BadHeaderError, send_mail
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from usuario.models import Usuario as User


def send_email(email, message, subject):
        recipient_list = [email]

        print(email, message, subject)

        try:
            send_mail(
                subject,
                message,
                recipient_list=recipient_list,
                from_email="lucasantonete.ifc@gmail.com",
            )
    
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        except ValidationError as e:
            return HttpResponse(str(e))
        return HttpResponse(
            {"message": "Email enviado com sucesso"}, status=status.HTTP_200_OK
        )


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def forget_password(request):
    email = request.data.get("email")
    try:
        user = User.objects.get(email=email)
    except user.DoesNotExist:
        return Response({"error": "Email não cadastrado"}, status=400)
        pass
    else:
        if(user.password_reset_token is not None):
             user.password_reset_token = None

                   
        # Gerar token exclusivo
        desired_length = 6
        token_size = (desired_length + 1) // 2 
        token = secrets.token_hex(token_size)[:desired_length]
        # Salvar o token, e-mail do usuário e data/hora
        user.password_reset_token = token
        user.password_reset_token_created = datetime.now(pytz.timezone('America/Sao_Paulo'))
        user.save()

        print(user.password_reset_token_created)
        
        send_email(email, token, "Redefinição de senha")

        response_data = {
            "id": user.id,
            "token": token,
            "message": "E-mail enviado com sucesso!",
        }
        # Exibir uma mensagem de sucesso na tela
        return Response(response_data, status=status.HTTP_200_OK)
    
TOKEN_EXPIRATION_SECONDS = 1200 


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def reset_password(request):
    # Procurar usuário com base no token
    new_password = request.data.get("new_password")
    token = request.data.get("token")

    try:
        user = User.objects.get(password_reset_token=token)  # Alterar para 'id=usuario_id'
    except User.DoesNotExist:
        return Response(
            {"message": "Token invalido ou esgotado."}, status=status.HTTP_404_NOT_FOUND
        )

    if user.password_reset_token_created:
        timezone = pytz.timezone('America/Sao_Paulo')
        current_time = datetime.now(timezone)
        expiration_time = current_time - user.password_reset_token_created
        
        print(expiration_time.total_seconds())
        if expiration_time.total_seconds() > TOKEN_EXPIRATION_SECONDS:
            user.password_reset_token = None
            user.password_reset_token_created = None
            user.save()
            return Response(
                {"message": "Token expirado."},
                status=status.HTTP_400_BAD_REQUEST,
            )
            
    # Atualizar a senha do usuário
    user.set_password(new_password)
    user.save()

    user.password_reset_token = ""
    user.password_reset_token_created = None
    user.save()

    return Response(
        {"message": "Senha atualizada com sucesso."}, status=status.HTTP_200_OK
    )