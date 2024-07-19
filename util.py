def assert_answer(want, got, *args):
    if len(args) > 0:
        print("inputs:")
        for data in args:
            print(data)
        print()

    print(f"want: {want}\ngot:  {got}")

    if want != got:
        print("outcome:  failed")
        exit("FAIL")

    print("outcome: success")
