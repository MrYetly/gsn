from rest_framework import serializers
from gsndb.models import District, School, Student, Course, Calendar, Grade, Attendance, Behavior, Referral
from user_app.models import CustomUser
from user_app.serializers import CustomUserSerializer

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = (
            "id",
            "code",
            "city",
            "state",
            "name",
            )

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            "id",
            "district",
            "name",
        )

class StudentSerializer(serializers.ModelSerializer):
    current_school = SchoolSerializer()

    class Meta:
        model = Student
        fields = (
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "current_school",
            "birthdate",
            "gender",
            "grade_year",
            "current_program",
            "reason_in_program",
            "state_id",
        )

class MyStudentsSerializer(serializers.ModelSerializer):
    current_school = SchoolSerializer(read_only = True)

    class Meta:
        model = Student
        fields = (
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "current_school",
            "birth_date",
        )

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = (
            "id",
            "year",
            "term",
        )

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "school",
            "name",
            "code",
            "subject",
        )

class BehaviorSerializer(serializers.ModelSerializer):
    context = serializers.CharField(source= "behavior_context")
    date = serializers.DateTimeField(format= "%-m/%-d/%-Y", source= 'behavior_incident_date_time')
    result = serializers.CharField(source= "behavior_result")
    class Meta:
        model = Behavior
        fields = (
            "id",
            "student",
            "school",
            "calendar",
            "incident_datetime",
            "context",
            "incident_type_program",
            "incident_result_program",
            "incident_type_school",
            "incident_result_school",
        )

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = (
            "id",
            "student",
            "course",
            "calendar",
            "entry_datetime",
            "grade",
            "term_final_value",
        )

class GradeForStudentSerializer(serializers.ModelSerializer):
    grade_set = GradeSerializer(many = True, read_only = True)

    class Meta:
        model = Student
        fields = (
            "id",
            "first_name",
            "last_name",
            "grade_set",
        )

class AttendanceSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format= "%-m/%-d/%-Y", source= 'attendance_data_entry_time')
    unexcused = serializers.CharField(source= 'attendance_total_unexcused_absences')
    excused = serializers.CharField(source= 'attendance_total_excused_absences')
    tardies = serializers.CharField(source= 'attendance_total_tardies')
    class Meta:
        model = Attendance
        fields = (
            "id",
            "student",
            "school",
            "calendar",
            "entry_date_time",
            "total_unexabs",
            "total_exabs",
            "total_tardies",
            "avg_daily_attendance",
            "term_final_value",
        )

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = (
            "id",
            "user",
            "student",
            "type",
            "date_given",
            "reference_name",
            "reference_phone",
            "reference_address",
        )
