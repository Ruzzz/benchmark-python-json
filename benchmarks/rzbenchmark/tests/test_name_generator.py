from .._core import NameGenerator


def _fn0():
    pass


class _Cls0:
    def simple_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass


def test_name_generator():
    name_generator = NameGenerator()
    assert name_generator(lambda x: x) == 'lambda'
    assert name_generator(lambda x: x) == 'lambda-2'

    def local_fn1():
        pass

    class LocalCls1:
        def simple_method(self):
            pass

        @classmethod
        def class_method(cls):
            pass

        @staticmethod
        def static_method():
            pass

    assert name_generator(local_fn1) == 'local_fn1'
    assert name_generator(LocalCls1.simple_method) == 'LocalCls1.simple_method'
    assert name_generator(LocalCls1.class_method) == 'LocalCls1.class_method'
    assert name_generator(LocalCls1.static_method) == 'LocalCls1.static_method'

    assert name_generator(_fn0) == '_fn0'
    assert name_generator(_Cls0.simple_method) == '_Cls0.simple_method'
    assert name_generator(_Cls0.class_method) == '_Cls0.class_method'
    assert name_generator(_Cls0.static_method) == '_Cls0.static_method'
