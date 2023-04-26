"""Soluciones a ecuaciones de una variable"""
from sympy import symbols, init_printing, Symbol, sympify, diff

init_printing(use_unicode=True)


def busqueda_incremental(str_f: str, dx: float, xi: float, n_max: int) -> tuple[float | None, float | None]:
    """Retorna cota donde puede estar el intervalo
    dx es lo que se mueve xi"""
    x: Symbol = symbols("x")
    sym_f = sympify(str_f)
    def f(c=None, f=sym_f, x=x): return f.subs(x, c)
    f_xi = f(xi)
    if f_xi == 0:
        print(f"{xi} es raiz")
        return None, xi
    cont = 0
    xf = xi+dx
    f_xf = f(xf)
    while f(xi)*f(xf) > 0 and cont < n_max:
        fxi = f(xi)
        fxf = f(xf)
        xi = xf
        xf += dx
        cont += 1
    fm = f_xi*f_xf
    if fm == 0:
        print(f"{xf} es raiz")
        return None, xf
    elif fm < 0:
        # :2f es para imprimir con dos decimales
        print(
            f"Hay raiz entre x={xi:2f}:f(x)={f_xi:2f} y x={xf:2f}:f(x)={f_xf:2f}")
        return xi, xf
    else:
        print("fail")
        return None, None


def bisect(xi, xf, str_f: str, tol) -> tuple[float, float, int]:
    """Busca raiz de str_f en [xi,xf] con una tolerancia tol
    si hay raices, primero se retornará xi, luego xf, luego la primera raíz posible por el 
    método de bisección"""
    x: Symbol = symbols("x")
    sym_f = sympify(str_f)
    def f(c=None, f=sym_f, x=x): return f.subs(x, c)

    # Algoritmo de bisección
    f_xi = f(xi)
    if f_xi == 0:
        return xi, 0, 0
    f_xf = f(xf)
    if f_xf == 0:
        return xf, 0, 0
    product = f_xi*f_xf
    if product == 0:
        print("one of the things is a root")
    elif product > 0:
        raise ValueError("Algo salió mal")

    xm = (xi+xf)/2
    f_xm = f(xm)
    if f_xm == 0:
        print("une raize")
        return xm, 0, 1
    count = 1
    error = tol+1
    while error >= tol:
        count += 1
        if f(xi)*f(xm) < 0:
            xf = xm
        else:
            xi = xm
        xm = (xi+xf)/2
        error = abs(xf-xm)
        # print( f"xi: {xi}, xf: {xf}, xm: {xm}, f_xi: {f(xi)},f_xf: {f(xf)}, f_xm: {f(xm)}")
    if f_xm == 0:
        print("une raize")
        return xm, 0, count
    else:
        print("aprox")
    return xm, error, count


def regla_falsa(xi: float, xf: float, str_f: str, tol: float):
    """ """
    # FIXME la optimización de wikipedia
    x: Symbol = symbols("x")
    sym_f = sympify(str_f)
    def f(c=None, f=sym_f, x=x): return f.subs(x, c)
    f_xi = f(xi)
    if f_xi == 0:
        return xi, 0
    f_xf = f(xf)
    if f_xf == 0:
        return xf, 0
    product = f_xi*f_xf
    if product == 0:
        print("one of the things is a root")
    elif product > 0:
        raise ValueError("Algo salió mal")

    def punto_inferior(a, b, f):
        return (f(b)*a-f(a)*b)/(f(b)-f(a))

    xm = punto_inferior(xi, xf, f)
    f_xm = f(xm)
    if f_xm == 0:
        print("une raize")
        return xm, 0

    error = tol+1, tol+1
    while max(error) >= tol:
        if f(xi)*f(xm) < 0:
            xf = xm
        else:
            xi = xm
        xm = punto_inferior(xi, xf, f)
        # FIXME este no es el error en regula falsi
        error = abs(xi-xm), abs(xf-xm)

        # print(
        #    f"xi: {xi}, xf: {xf}, xm: {xm}, f_xi: {f(xi)}, f_xf: {f(xf)}, f_xm: {f(xm)}")

    if f(xm) == 0:
        print("une raize")
        return xm, 0
    else:
        print("aprox")
    return xm, error


def punto_fijo(str_f, str_g, x0, tol, Nmax):
    x: Symbol = symbols("x")
    sym_f = sympify(str_f)
    sym_g = sympify(str_g)
    def f(c=None, f=sym_f, x=x): return f.subs(x, c)
    def g(c=None, df=sym_g, x=x): return g.subs(x, c)
    error, conteo = abs(x0-g(x0)), 0
    xi = x0
    while error >= tol and conteo < Nmax:
        xi1 = g(xi)
        error, conteo = abs(xi-g(x0)), conteo+1
        xi = xi1


def newton(str_f, x0, tol, Nmax):
    """Si es doblemente diferenciable, siempre converge
    Interesante:  """
    # FIXME EARLY RETURNS
    x: Symbol = symbols("x")
    sym_f = sympify(str_f)
    sym_df = diff(sym_f, x, 1)
    def f(c=None, f=sym_f, x=x): return f.subs(x, c)
    def df(c=None, df=sym_df, x=x): return df.subs(x, c)
    xi = x0
    error, conteo = tol+1, 0
    bilateral = True
    changed = False
    while error > tol+1 and conteo < Nmax:
        xi1 = xi - f(xi)/df(xi)
        error, conteo = abs(xi-xi1), conteo+1
        xi = xi1
    if error < tol:
        return xi, error, conteo
    else:
        print("Error")


def secante(str_f, x0, x1, tol, nmax):
    """No tiene que contener raiz"""
    x: Symbol = symbols("x")
    sym_f = sympify(str_f)
    sym_df = diff(sym_f, x, 1)
    def f(c=None, f=sym_f, x=x): return f.subs(x, c)
    def xin(xi, xi1): xi1-(f(xi1)*(xi1-xi))/(f(xi1)-f(xi))
    xi = x0
    xi1 = x1
    error,conteo = tol +1, 0
    
    while error > tol+1 and conteo < nmax:
        xi2 = xin(xi, xi1)
        error, conteo = abs(xi-xi1), conteo+1
        xi = xi1


def raices_multiples(str_f, str_fp, str_fpp, tol, Nmax):
    """es más lento pero converge igual de newton"""
    x: Symbol = symbols("x")
    sym_f = sympify(str_f)
    sym_df = sympify(str_fp)
    sym_ddf = sympify(str_fpp)
    def f(c=None, f=sym_f, x=x): return f.subs(x, c)
    def df(c=None, df=sym_df, x=x): return df.subs(x, c)
    def ddf(c=None, ddf=sym_ddf, x=x): return ddf.subs(x, c)


def multiplicidad(strf, r):
    x: Symbol = symbols("x")
    sym_f = sympify(strf)
    def f(c=None, f=sym_f, x=x): return f.subs(x, c)
    def df(c=None, df=sym_f, x=x): return diff(df, x).subs(x, c)
    if abs(f(r)) != 0:
        return 0
    print(f(r))
    m = 1
    print(sym_df := diff(sym_f, x))
    print(f(r,sym_df))
    while f(r, sym_df) == 0:
        m += 1
        print(f"m = {m}")
        print(sym_df := diff(sym_df, x))
        print(f"f({r}) = {f(r, sym_df)}")
    return m
