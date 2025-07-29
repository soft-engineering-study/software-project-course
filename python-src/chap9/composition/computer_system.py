"""
Demonstrating composition with a Computer System.
Shows how complex objects are built from simpler components.
"""

class CPU:
    """Central Processing Unit component."""
    
    def __init__(self, brand, model, cores, speed_ghz):
        self.brand = brand
        self.model = model
        self.cores = cores
        self.speed_ghz = speed_ghz
        self.temperature = 30  # Celsius
        
    def process(self, task):
        """Process a task and increase temperature."""
        self.temperature += 5
        return f"Processing {task} on {self.cores} cores at {self.speed_ghz}GHz"
        
    def cool_down(self):
        """Cool down the CPU."""
        if self.temperature > 30:
            self.temperature -= 10
            
    def get_info(self):
        """Get CPU information."""
        return f"{self.brand} {self.model} - {self.cores} cores @ {self.speed_ghz}GHz"


class RAM:
    """Random Access Memory component."""
    
    def __init__(self, capacity_gb, speed_mhz, ram_type='DDR4'):
        self.capacity_gb = capacity_gb
        self.speed_mhz = speed_mhz
        self.ram_type = ram_type
        self.used_gb = 0
        
    def allocate(self, size_gb):
        """Allocate memory."""
        if self.used_gb + size_gb <= self.capacity_gb:
            self.used_gb += size_gb
            return f"Allocated {size_gb}GB of RAM"
        return "Insufficient memory!"
        
    def free(self, size_gb):
        """Free memory."""
        self.used_gb = max(0, self.used_gb - size_gb)
        return f"Freed {size_gb}GB of RAM"
        
    def get_usage(self):
        """Get memory usage information."""
        free_gb = self.capacity_gb - self.used_gb
        usage_percent = (self.used_gb / self.capacity_gb) * 100
        return f"Memory: {self.used_gb}/{self.capacity_gb}GB used ({usage_percent:.1f}%)"


class Storage:
    """Storage device component."""
    
    def __init__(self, capacity_gb, storage_type='SSD', read_speed_mbps=500):
        self.capacity_gb = capacity_gb
        self.storage_type = storage_type
        self.read_speed_mbps = read_speed_mbps
        self.used_gb = 0
        self.files = []
        
    def save_file(self, filename, size_gb):
        """Save a file to storage."""
        if self.used_gb + size_gb <= self.capacity_gb:
            self.used_gb += size_gb
            self.files.append({'name': filename, 'size': size_gb})
            return f"Saved {filename} ({size_gb}GB)"
        return "Insufficient storage space!"
        
    def delete_file(self, filename):
        """Delete a file from storage."""
        for file in self.files:
            if file['name'] == filename:
                self.used_gb -= file['size']
                self.files.remove(file)
                return f"Deleted {filename}"
        return "File not found!"
        
    def list_files(self):
        """List all files in storage."""
        if not self.files:
            return "No files stored"
        return "\n".join([f"- {f['name']} ({f['size']}GB)" for f in self.files])


class GPU:
    """Graphics Processing Unit component."""
    
    def __init__(self, brand, model, memory_gb):
        self.brand = brand
        self.model = model
        self.memory_gb = memory_gb
        self.is_active = False
        
    def render(self, application):
        """Render graphics for an application."""
        self.is_active = True
        return f"GPU rendering graphics for {application}"
        
    def stop_rendering(self):
        """Stop rendering."""
        self.is_active = False
        return "GPU rendering stopped"


class Computer:
    """A computer system demonstrating composition with multiple components."""
    
    def __init__(self, name, cpu, ram, storage, gpu=None):
        self.name = name
        self.cpu = cpu  # Composition: Computer HAS-A CPU
        self.ram = ram  # Composition: Computer HAS-A RAM
        self.storage = storage  # Composition: Computer HAS-A Storage
        self.gpu = gpu  # Optional composition: Computer MAY-HAVE-A GPU
        self.is_on = False
        self.running_programs = []
        
    def power_on(self):
        """Turn on the computer."""
        if not self.is_on:
            self.is_on = True
            # Initialize system with some RAM usage
            self.ram.allocate(2)  # OS uses 2GB
            return f"{self.name} is powering on... System ready!"
        return "Computer is already on"
        
    def power_off(self):
        """Turn off the computer."""
        if self.is_on:
            self.is_on = False
            self.running_programs.clear()
            self.ram.used_gb = 0
            if self.gpu and self.gpu.is_active:
                self.gpu.stop_rendering()
            return f"{self.name} is shutting down..."
        return "Computer is already off"
        
    def run_program(self, program_name, ram_required, use_gpu=False):
        """Run a program on the computer."""
        if not self.is_on:
            return "Computer must be on to run programs"
            
        # Check RAM availability
        ram_result = self.ram.allocate(ram_required)
        if "Insufficient" in ram_result:
            return ram_result
            
        # Start the program
        self.running_programs.append(program_name)
        result = f"Starting {program_name}...\n"
        result += self.cpu.process(program_name) + "\n"
        result += ram_result
        
        # Use GPU if requested and available
        if use_gpu and self.gpu:
            result += "\n" + self.gpu.render(program_name)
        elif use_gpu and not self.gpu:
            result += "\nNo GPU available for graphics acceleration"
            
        return result
        
    def close_program(self, program_name):
        """Close a running program."""
        if program_name in self.running_programs:
            self.running_programs.remove(program_name)
            self.ram.free(2)  # Simplified: assume each program uses 2GB
            result = f"Closed {program_name}"
            if self.gpu and self.gpu.is_active:
                result += "\n" + self.gpu.stop_rendering()
            return result
        return f"{program_name} is not running"
        
    def get_system_info(self):
        """Get complete system information."""
        info = f"=== {self.name} System Information ===\n"
        info += f"Status: {'On' if self.is_on else 'Off'}\n"
        info += f"CPU: {self.cpu.get_info()} (Temp: {self.cpu.temperature}°C)\n"
        info += f"RAM: {self.ram.capacity_gb}GB {self.ram.ram_type} @ {self.ram.speed_mhz}MHz\n"
        info += f"     {self.ram.get_usage()}\n"
        info += f"Storage: {self.storage.capacity_gb}GB {self.storage.storage_type} "
        info += f"({self.storage.used_gb}GB used)\n"
        if self.gpu:
            info += f"GPU: {self.gpu.brand} {self.gpu.model} ({self.gpu.memory_gb}GB)\n"
        if self.running_programs:
            info += f"Running Programs: {', '.join(self.running_programs)}"
        return info


# Example usage
if __name__ == "__main__":
    # Create computer components
    intel_cpu = CPU('Intel', 'Core i7-12700K', 12, 3.6)
    corsair_ram = RAM(32, 3600, 'DDR4')
    samsung_ssd = Storage(1000, 'NVMe SSD', 3500)
    nvidia_gpu = GPU('NVIDIA', 'RTX 3080', 10)
    
    # Build a gaming computer using composition
    gaming_pc = Computer('Gaming Beast', intel_cpu, corsair_ram, samsung_ssd, nvidia_gpu)
    
    print("=== Computer Composition Example ===")
    print(gaming_pc.get_system_info())
    
    print("\n--- Using the computer ---")
    print(gaming_pc.power_on())
    print()
    
    # Save some files
    print(gaming_pc.storage.save_file('game.exe', 50))
    print(gaming_pc.storage.save_file('documents.zip', 5))
    
    # Run programs
    print("\n" + gaming_pc.run_program('Web Browser', 4))
    print("\n" + gaming_pc.run_program('Video Game', 8, use_gpu=True))
    
    print("\n" + gaming_pc.get_system_info())
    
    # Create a workstation without GPU
    print("\n\n--- Building a workstation ---")
    amd_cpu = CPU('AMD', 'Ryzen 9 5950X', 16, 3.4)
    crucial_ram = RAM(64, 3200, 'DDR4')
    wd_ssd = Storage(2000, 'SSD', 550)
    
    workstation = Computer('Workstation Pro', amd_cpu, crucial_ram, wd_ssd)  # No GPU
    print(workstation.get_system_info())
    print(workstation.power_on())
    print(workstation.run_program('Code Editor', 6, use_gpu=True))  # Requests GPU but none available