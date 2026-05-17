from newTrainFile import add
from newTrainFile import get_system_status

def test_add():
    assert add("Hello", "World") == "HelloWorld"
   
def test_get_system_status():
    status = get_system_status()
    
    assert isinstance(status, tuple)
    assert len(status) == 3
    assert status[0] >= 0
