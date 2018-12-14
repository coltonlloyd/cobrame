from symengine import Symbol as SymengineSymbol
from sympy.core.add import Add as SympyAdd
from sympy.core.power import Pow as SympyPow
from sympy.core.mul import Mul as SympyMul
from sympy.core.expr import Expr as SympyExpr
from sympy import LessThan

class Expr(SympyExpr):
    pass


class Symbol(SymengineSymbol):
    def __init__(self, name, *args, **kwargs):
        super(Symbol, self).__init__(name)
        self._name = name

    def __le__(self, other):
        val = self.subs(self, .01)
        return super(Symbol, self.__class__).__le__(val, other)

    def __lt__(self, other):
        val = self.subs(self, .01)
        return super(Symbol, self.__class__).__le__(val, other)

    def __gt__(self, other):
        val = self.subs(self, .01)
        return super(Symbol, self.__class__).__le__(val, other)

    def __ge__(self, other):
        val = self.subs(self, .01)
        return super(Symbol, self.__class__).__le__(val, other)

    def __add__(self, other):
        return Add(self, other)

    def __radd__(self, other):
        return Add(other, self)

    def __sub__(self, other):
        return Add(self, -other)

    def __rsub__(self, other):
        return Add(other, -self)

    def __pow__(self, other):
        return Pow(self, other)

    def __rpow__(self, other):
        return Pow(other, self)

    def __mul__(self, other):
        return Mul(self, other)

    def __rmul__(self, other):
        return Mul(other, self)


class Mul(SympyMul):
    def __le__(self, other):
        val = self.subs(self, .01)
        return super(Mul, self.__class__).__le__(val, other)

    def __lt__(self, other):
        val = self.subs(self, .01)
        return super(Mul, self.__class__).__lt__(val, other)

    def __gt__(self, other):
        val = self.subs(self, .01)
        return super(Mul, self.__class__).__gt__(val, other)

    def __ge__(self, other):
        val = self.subs(self, .01)
        return super(Mul, self.__class__).__ge__(val, other)


class Add(SympyAdd):

    def __le__(self, other):
        val = self.subs(self, .01)
        return super(Add, self.__class__).__le__(val, other)

    def __lt__(self, other):
        val = self.subs(self, .01)
        return super(Add, self.__class__).__lt__(val, other)

    def __gt__(self, other):
        val = self.subs(self, .01)
        return super(Add, self.__class__).__gt__(val, other)

    def __ge__(self, other):
        val = self.subs(self, .01)
        return super(Add, self.__class__).__ge__(val, other)


class Pow(SympyPow):
    def __le__(self, other):
        val = self.subs(self, .01)
        return super(Pow, self.__class__).__le__(val, other)

    def __lt__(self, other):
        val = self.subs(self, .01)
        return super(Pow, self.__class__).__le__(val, other)

    def __gt__(self, other):
        val = self.subs(self, .01)
        return super(Pow, self.__class__).__le__(val, other)

    def __ge__(self, other):
        val = self.subs(self, .01)
        return super(Pow, self.__class__).__le__(val, other)