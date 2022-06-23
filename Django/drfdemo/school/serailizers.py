from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from school.models import Teacher, Student, Achievement, Course

"""
默认情况下，模型经过序列化器数据转换，对于外键信息仅仅把数据库里面的外键ID返回
所以总结序列化嵌套有三个方法：
1、不停在各个序列化class 当中加入查询的序列化外键 course = CourseModelSerializer() s_achievement = AchievementModelSerializer(many=True)
2、使用depth 方式
3、使用teacher_name = serializers.CharField(source="course.teacher.name")
4、修改model     def Achievement(self): 类似这个方法

"""


class CourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class AchievementModelSerializer(ModelSerializer):
    """
    序列化嵌套两种方式
    1、使用 course_name =serializers.CharField(source="course.name") 类似这样方法
    2、使用 course = CourseModelSerializer() 不停嵌套
    """
    # course = CourseModelSerializer()
    course_name = serializers.CharField(source="course.name")
    teacher_name = serializers.CharField(source="course.teacher.name")

    class Meta:
        model = Achievement
        # fields=['score']
        # fields = ['id', 'course', 'score', 'create_time']
        fields = ['id', 'course_name', 'score', 'create_time', 'teacher_name']


class TeacherModelSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class AchievementModelSerializer2(ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"
        # fields = ['id', 'course_name', 'score', 'create_time', 'teacher_name']
        depth = 2
        """
        指定关联深度
        从老师model > 课程 = 1
        从老师model > 课程 > 成绩 = 2
        从老师model > 课程 > 成绩 > 学生= 3
        """

        # depth = 1
        # 会去找是外键的字段然后序列化
        # 1 代表的是序列化的深度,意思就是序列化的的数据表中加入还有关联的外键是否序列化

class StudentModelSerializer(ModelSerializer):
    """
    s_achievement 这个必须和模型声明外键必须一致，非外键字段不能指定序列化选项
    s_achievement 在 Achievement table 属于外键所以必须要这么使用
    many=True 输入的列表
    """
    # s_achievement = AchievementModelSerializer(many=True)
    # s_achievement = AchievementModelSerializer2(many=True)

    class Meta:
        model = Student
        # fields = "__all__"
        # fields = ['id', 'name', 'sex', 's_achievement', ]
        fields = ['id', 'name', 'sex', 'Achievement', ]
