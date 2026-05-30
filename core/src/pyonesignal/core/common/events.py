from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CallbackProducer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/events/CallbackProducer"
    __javaconstructor__ = [("()V", False)]
    set = JavaMethod("(Ljava/lang/Object;)V")
    getHasCallback = JavaMethod("()Z")
    fire = JavaMethod("(Lkotlin/jvm/functions/Function1;)V")
    fireOnMain = JavaMethod("(Lkotlin/jvm/functions/Function1;)V")
    suspendingFire = JavaMethod("(Lkotlin/jvm/functions/Function2;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    suspendingFireOnMain = JavaMethod("(Lkotlin/jvm/functions/Function2;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$getCallback$p = JavaStaticMethod("(Lcom/onesignal/common/events/CallbackProducer;)Ljava/lang/Object;")

class EventProducer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/events/EventProducer"
    __javaconstructor__ = [("()V", False)]
    fire = JavaMethod("(Lkotlin/jvm/functions/Function1;)V")
    fireOnMain = JavaMethod("(Lkotlin/jvm/functions/Function1;)V")
    suspendingFire = JavaMethod("(Lkotlin/jvm/functions/Function2;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    suspendingFireOnMain = JavaMethod("(Lkotlin/jvm/functions/Function2;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getHasSubscribers = JavaMethod("()Z")
    subscribe = JavaMethod("(Ljava/lang/Object;)V")
    unsubscribe = JavaMethod("(Ljava/lang/Object;)V")
    subscribeAll = JavaMethod("(Lcom/onesignal/common/events/EventProducer;)V")
    access$getSubscribers$p = JavaStaticMethod("(Lcom/onesignal/common/events/EventProducer;)Ljava/util/List;")

class ICallbackNotifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/events/ICallbackNotifier"
    set = JavaMethod("(Ljava/lang/Object;)V")
    getHasCallback = JavaMethod("()Z")

class IEventNotifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/events/IEventNotifier"
    getHasSubscribers = JavaMethod("()Z")
    subscribe = JavaMethod("(Ljava/lang/Object;)V")
    unsubscribe = JavaMethod("(Ljava/lang/Object;)V")