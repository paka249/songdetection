import pyaudio  # For recording audio from microphone
import wave     # For saving audio as WAV files
import numpy as np  # For handling audio data as arrays

class AudioRecorder:           # Our main audio recorder class
    def __init__(self):        # Constructor - runs when you create AudioRecorder() 
        # Audio settings (CD quality)
        self.SAMPLE_RATE = 44100       # 44,100 samples per second (
        self.CHANNELS = 1              # Mono recording (1 channel)
        self.FORMAT = pyaudio.paInt16  # 16-bit signed integers
        
    def record(self, duration_seconds):
        
        print(f"Recording for {duration_seconds} seconds...")
        
        # Initialize PyAudio
        audio = pyaudio.PyAudio()
        
        # Open microphone stream
        stream = audio.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.SAMPLE_RATE,
            input=True

        )
        
        # Calculate how many samples we need
        total_samples = int(self.SAMPLE_RATE * duration_seconds)
        
        # Record the audio
        print("Recording started...")
        audio_data = stream.read(total_samples)
        
        # Clean up - close stream and audio
        stream.close()
        audio.terminate()
        
        # Convert to numpy array for easier processing
        audio_array = np.frombuffer(audio_data, dtype=np.int16)
        
        print("Recording finished!")
        return audio_array

# Test our recorder
if __name__ == "__main__":
    # Create recorder
    recorder = AudioRecorder()
    
    # Record 3 seconds of audio
    audio_data = recorder.record(3.0)

    # Show the audio sample information
    print(f"Recorded {len(audio_data)} audio samples")
    print(f"Duration: {len(audio_data) / 44100:.2f} seconds")
    

    """

    # Optional: Print some audio statistics
     
    print(f"\nFirst 20 audio samples: {audio_data[:20]}")
    print(f"Last 20 audio samples: {audio_data[-20:]}")
    print(f"Max amplitude: {np.max(audio_data)}")
    print(f"Min amplitude: {np.min(audio_data)}")
    print(f"Average amplitude: {np.mean(audio_data):.2f}")
    
    """
    
    
    print("Recording complete!")
    







