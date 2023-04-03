from typing import Any, List

from scanner import getYAMLFiles, isValidUserName, isValidPasswordName, isValidKey, checkIfValidSecret

def fuzzMethod (method, args: List[Any]):
    for arg in args:
        print("---------------------------------------------------------------------------")
        try:
            result = method(*arg)
        except Exception as e:
            print(f"Fuzz result: method \"{method.__name__}\" failed: {e}")
        else:
            print(f"Fuzz result: method \"{method.__name__}\" passed: {result}")

if __name__=="__main__":
    fuzzInputs = [
        (
            getYAMLFiles, [
                ("bad",),
                (1,),
                (1.0,),
                ([],),
                ({},),
                (None,)
            ]
        ),
        (
            isValidUserName, [
                ("domain",),
                (1,),
                (1.0,),
                ([],),
                ({},),
                (None,)
            ]
        ),
        (
            isValidPasswordName, [
                ("_auth",),
                (1,),
                (1.0,),
                ([],),
                ({},),
                (None,)
            ]
        ),
        (
            isValidKey, [
                ("bad",),
                (1,),
                (1.0,),
                ([],),
                ({},),
                (None,)
            ]
        ),
        (
            checkIfValidSecret, [
                (":undef",),
                (1,),
                (1.0,),
                ([],),
                ({},),
                (None,)        
            ]
        )
    ]
    for method, args in fuzzInputs:
        fuzzMethod(method, args)