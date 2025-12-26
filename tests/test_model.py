from app.model import model_instance

def test_model_logic():
    # Setup
    model_instance.load_model()
    
    # Test
    result = model_instance.predict("Happy day!")
    
    # Assert
    assert "label" in result
    assert "score" in result