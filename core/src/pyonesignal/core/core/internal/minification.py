from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class KeepStub(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/minification/KeepStub"