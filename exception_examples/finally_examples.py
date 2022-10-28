
i = 0
print("_" * 40)
print(f"{i=}: Finally executes when there is no exception.")
try:
    print(f"No exceptions at {i=}")
finally:
    print(f"Cleaning up for {i=}")


i += 1
print("_" * 40)
print(f"{i=}: Finally executes when there is a caught exception.")
try:
    a = i / 0
except ZeroDivisionError as e:
    print(f"Caught exception for {i=}: {e}")
finally:
    print(f"Cleaning up for {i=}")


i += 1
print("_" * 40)
print(f"{i=}: Finally executes when there is an uncaught exception.")
# Nest the demonstration block in another try so we can keep demonstrating
try:
    # Note the behavior in this try/except/finally
    try:
        print(f"Uncaught exception for {i=}")
        a = i/0
    finally:
        print(f"Cleaning up for {i=}")
except ZeroDivisionError:
    pass


i += 1
print("_" * 40)
print(f"{i=}: Finally executes before a continue.")
for n in range(-1, 2):
    try:
        a = i/n
    except ZeroDivisionError as e:
        print(f"Exception at {i=}, {n=}, continuing in loop.")
        continue
    finally:
        print(f"Cleaning up for {i=}, {n=}")


i += 1
print("_" * 40)
print(f"{i=}: Finally executes before a break.")
for n in range(-1, 2):
    try:
        a = i/n
    except ZeroDivisionError as e:
        print(f"Exception at {i=}, {n=}, stopping loop.")
        break
    finally:
        print(f"Cleaning up for {i=}, {n=}")


i += 1
print("_" * 40)
print(f"{i=}: Finally executes before a return.")
def f():
    try:
        return None
    finally:
        print(f"Cleaning up for {i=}")
f()


i += 1
print("_" * 40)
print(f"{i=}: Finally executes when another exception occurs inside except block.")
# Nest the demonstration block in another try so we can keep demonstrating
try:
    # Note the behavior in this try/except/finally
    try:
        a = i/0
    except ZeroDivisionError:
        print("NameError occured while handling ZeroDivisionError")
        a = INVALID_SYMBOL
    finally:
        print(f"Cleaning up for {i=}")
except NameError:
    pass


i += 1
print("_" * 40)
print(f"{i=}: Finally executes when an exception occurs inside try's else block.")
# Nest the demonstration block in another try so we can keep demonstrating
try:
    # Note the behavior in this try/except/finally
    try:
        pass
    except Exception:
        # Unreachable
        pass
    else:
        print("Exception in try's else block.")
        a = i/0
    finally:
        print(f"Cleaning up for {i=}")
except ZeroDivisionError:
    pass