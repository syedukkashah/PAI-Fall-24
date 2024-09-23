class InstanceCounter:
    # Class variable to store the count of instances
    instance_count = 0
    
    def __init__(self):
        # Increment the count each time a new instance is created
        InstanceCounter.instance_count += 1
    
    # Method to return the current instance count
    @classmethod
    def get_instance_count(cls):
        return cls.instance_count

# Create two instances
instance1 = InstanceCounter()
instance2 = InstanceCounter()

# Print the count of instances created
print(f"Number of instances created: {InstanceCounter.get_instance_count()}")
