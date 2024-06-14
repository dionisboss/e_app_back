# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import uvicorn
import logging


request_logger = logging.getLogger("request_logger")
request_logger.setLevel(logging.DEBUG)

request_file_handler = logging.FileHandler("request.log")
request_file_handler.setLevel(logging.DEBUG)

request_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
request_file_handler.setFormatter(request_formatter)

request_logger.addHandler(request_file_handler)

class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        request_logger.debug(f"Request: {request.method} {request.url}")

        response = await call_next(request)

        request_logger.debug(f"Response: {response.status_code}")

        return response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,  
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

app.add_middleware(RequestLoggerMiddleware)


"""
    
import admin routes

"""

from api.endpoints.admin.business_profiles import router as business_profiles_admin_router
from api.endpoints.admin.locations import router as locations_admin_router
from api.endpoints.admin.offices import router as offices_admin_router
from api.endpoints.admin.locks import router as locks_admin_router
from api.endpoints.admin.lock_systems import router as lock_systems_admin_router
from api.endpoints.admin.renters import router as renters_admin_router
from api.endpoints.admin.office_types import router as office_types_admin_router
from api.endpoints.admin.users import router as users_admin_router
from api.endpoints.admin.user_roles import router as user_roles_admin_router
from api.endpoints.admin.billings import router as billings_admin_router
from api.endpoints.admin.rented_offices import router as rented_offices_admin_router
from api.endpoints.admin.hardware import router as hardware_admin_router
from api.endpoints.admin.document_templates import router as document_templates_admin_router


"""

import client routes

"""

from api.endpoints.client.locations import router as locations_client_router
from api.endpoints.client.offices import router as offices_client_router
from api.endpoints.client.renters import router as renters_client_router
from api.endpoints.client.users import router as users_client_router
from api.endpoints.client.billings import router as billings_client_router
from api.endpoints.client.locks import router as locks_client_router
from api.endpoints.client.telegram import router as telegram_client_router




"""

import auth routes

"""

from api.endpoints.admin.auth.authenticate import router as auth_admin_router
from api.endpoints.client.auth.authenticate import router as auth_client_router


"""

Including routers

"""

app.include_router(auth_admin_router, prefix="/admin/auth", tags=["admin/auth"])
app.include_router(business_profiles_admin_router, prefix="/admin/business-profiles", tags=["admin/business-profiles"])
app.include_router(locations_admin_router, prefix="/admin/locations", tags=["admin/locations"])
app.include_router(offices_admin_router, prefix="/admin/offices", tags=["admin/offices"])
app.include_router(locks_admin_router, prefix="/admin/locks", tags=["admin/locks"])
app.include_router(renters_admin_router, prefix="/admin/renters", tags=["admin/renters"])
app.include_router(lock_systems_admin_router, prefix="/admin/lock-systems", tags=["admin/lock-systems"])
app.include_router(office_types_admin_router, prefix="/admin/office-types", tags=["admin/office-types"])
app.include_router(users_admin_router, prefix="/admin/users", tags=["admin/users"])
app.include_router(user_roles_admin_router, prefix="/admin/user-roles", tags=["/admin/user-roles"])
app.include_router(billings_admin_router, prefix="/admin/billings", tags=["admin/billings"])
app.include_router(rented_offices_admin_router, prefix="/admin/rented-offices", tags=["admin/rented-offices"])
app.include_router(hardware_admin_router, prefix="/admin/hardware", tags=["admin/hardware"])
app.include_router(document_templates_admin_router, prefix="/admin/documentation/templates", tags=["admin/documentation-templates"])




app.include_router(auth_client_router, prefix="/client/auth", tags=["client/auth"])

app.include_router(locations_client_router, prefix="/client/locations", tags=["client/locations"])
app.include_router(offices_client_router, prefix="/client/offices", tags=["client/offices"])
app.include_router(renters_client_router, prefix="/client/renters", tags=["client/renters"])
app.include_router(users_client_router, prefix="/client/users", tags=["client/users"])
app.include_router(billings_client_router, prefix="/client/billings", tags=["client/billings"])
app.include_router(locks_client_router, prefix="/client/locks", tags=["client/locks"])
app.include_router(telegram_client_router, prefix="/client/telegram", tags=["client/telegram"])




if __name__ == "__main__":

    # uvicorn.run(app, host="95.213.216.205", port=8000, ssl_keyfile="cert.key", ssl_certfile="cert.crt")
    uvicorn.run(app, host="localhost", port=8000)
