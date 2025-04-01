from flask import Flask,send_from_directory,render_template
from flask import send_from_directory

from flask_restful import Resource, Api
from package.patient import Patients, Patient
from package.doctor import Doctors, Doctor
from package.appointment import Appointments, Appointment
from package.common import Common
from package.medication import Medication, Medications
from package.department import Departments, Department
from package.nurse import Nurse, Nurses
from package.room import Room, Rooms
from package.procedure import Procedure, Procedures 
from package.prescribes import Prescribes, Prescribe
from package.undergoes import Undergoess, Undergoes