class StarError(BaseException):
    def __init__(self, info=''):
        self.info = str(info)
    def __str__(self):
        return self.info

class Array:
    def __init__(self, lst):
        if isinstance(lst, type):
            self.__list = []
            self.__dtype = lst
            return
        if not lst:
            raise (
                StarError("lst argument cannot be empty"))
        self.__dtype = type(lst[0])
        if not hasattr(lst.__class__, '__iter__'):
            raise (
                StarError(f"lst argument must be Iterable, not {type(lst).__name__}"))
        self.__list = list(lst)
        for i, item in enumerate(lst):
            if type(item) is not self.__dtype:
                raise (
                   StarError(f"sequence item {i}, expected {self.__dtype.__name__}, got {type(item).__name__}"))
    def __str__(self):
        return f'Array({self.__list})'
                
    def __iter__(self):
        for item in self.__list:
            yield item
    def __contains__(self, val):
        return val in self.__list
        
    def __len__(self):
        return len(self.__list)
    def __getitem__(self, i):
        try:
            return self.__list[i]
        except:
            pass
        raise (
            StarError(f"invalid index {i}"))
    def __setitem__(self, i, new):
        if type(new) is not self.__dtype:
            raise (
                StarError(f"expected {self.__dtype.__name__}, got {type(new).__name__}"))
        try:
            self.__list[i] = new
        except:
            pass
        raise (
            StarError(f"invalid index {i}"))
        
    def __add__(self, other):
        try:
            return Array([x + other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __sub__(self, other):
        try:
            return Array([x - other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __mul__(self, other):
        try:
            return Array([x * other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __truediv__(self, other):
        try:
            return Array([x / other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __floordiv__(self, other):
        try:
            return Array([x // other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
        
    def __mod__(self, other):
        try:
            return Array([x % other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __divmod__(self, other):
        try:
            return Array([divmod(x, other) for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __pow__(self, other):
        try:
            return Array([x ** other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
        
    def __lshift__(self, other):
        try:
            return Array([x << other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __rshift__(self, other):
        try:
            return Array([x >> other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
        
    def __and__(self, other):
        try:
            return Array([x & other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __xor__(self, other):
        try:
            return Array([x ^ other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __or__(self, other):
        try:
            return Array([x | other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __not__(self):
        try:
            return Array([~x for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand"))

    def __eq__(self, other):
        try:
            return Array([x == other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __ne__(self, other):
        try:
            return Array([x != other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __gt__(self, other):
        try:
            return Array([x > other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __ge__(self, other):
        try:
            return Array([x >= other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __lt__(self, other):
        try:
            return Array([x < other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))
    def __le__(self, other):
        try:
            return Array([x <= other for x in self])
        except:
            pass
        raise (
            StarError(f"unsupported operand between Array and {type(other).__name__}"))

    def append(self, *newvals):
        for newval in newvals:
            if type(newval) is not self.__dtype:
                raise (
                    StarError(f"expected {self.__dtype.__name__}, got {type(newval).__name__}"))
        self.__list.extend(list(newvals))
    def remove(self, *vals):
        for i, val in enumerate(vals):
            if val not in self:
                raise (
                    StarError(f"sequence item {i}: {val!r} not in Array"))
        for item in vals:
            self.__list.remove(item)
    def pop(self, *indexes):
        for index in indexes:
            error = True
            try:
                self[index]
                error = False
            except:
                pass
            if error:
                raise (
                    StarError(f"invalid index {i}"))
        for i in indexes:
            self.__list.pop(i)
    def index(self, item):
        try:
            return self.__list.index(item)
        except:
            pass
        raise (
            StarError(f"{item!r} not in Array"))
    def count(self, item):
        return self.__list.count(item)

    @property
    def el(self):
        class El:
            def __init__(_self, lst, dtype):
                _self.__list = lst
                _self.__dtype = dtype
            def __getattr__(_self, x):
                attr = getattr(_self.__dtype, x)
                if not hasattr(attr, '__call__'):
                    try:
                        return Array([getattr(y, x) for y in _self.__list])
                    except:
                        pass
                    raise (
                        StarError(f"an error occurred"))
                def wrapper(*args, **kwargs):
                    try:
                        return Array([attr(x, *args, **kwargs) for x in _self.__list])
                    except:
                        pass
                    raise (
                        StarError(f"an error occurred"))
                return wrapper
        return El(self.__list, self.__dtype)
        
