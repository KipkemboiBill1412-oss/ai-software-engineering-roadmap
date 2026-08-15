marks=[55, 70, 83, 42, 91]
passed=0
failed=0
for mark in marks:
    if mark>=70:
        passed+=1
        print(f"{mark} Pass")
    else:
        failed+=1
        print(f"{mark} Fail")
print(f"Passed = {passed}")
print(f"Failed = {failed}")



