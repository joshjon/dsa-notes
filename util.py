def assert_answer(want, got, *args):
    if len(args) > 0:
        if len(args) == 1:
            print(f"input: {args[0]}")
        else:
            print("inputs:")
            for data in args:
                print(f"\t- {data}")

    print(f"want: {want}\ngot:  {got}")

    if want != got:
        print("outcome:  failed")
        exit("FAIL")

    print("outcome: success")
