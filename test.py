def test_print_message(capsys):
    # Call the function
    message = print_message()
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Check the printed message
    assert captured.out == "Hello, pytest!\n"
    
    # Verify the returned message
    assert message == "Hello, pytest!"
