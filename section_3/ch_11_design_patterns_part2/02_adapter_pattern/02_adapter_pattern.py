"""Adapter Pattern


The Adapter Pattern allows objects with incompatible interfaces to work together. It acts as a bridge by wrapping an existing class with a new interface that clients expect.

Here are two systems with incompatible interfaces:

class OldPrinter:
    def old_print(self, text):
        return f"OLD: {text}"

class NewPrinter:
    def print(self, text):
        return f"NEW: {text}"
The old printer uses old_print() while the new one uses print().

Create an adapter to make the old printer work with the new interface:

class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self, text):
        # Adapt old interface to new interface
        return self.old_printer.old_print(text)
The adapter wraps the old printer and provides the expected interface.

Use both printers with the same client code:

def print_document(printer, text):
    return printer.print(text)  # Expects print() method

# Use new printer directly
new_printer = NewPrinter()
print(print_document(new_printer, "Hello"))

# Use old printer through adapter
old_printer = OldPrinter()
adapter = PrinterAdapter(old_printer)
print(print_document(adapter, "Hello"))
Create another example with media players:

class Mp3Player:
    def play_mp3(self, filename):
        return f"Playing MP3: {filename}"

class Mp4Player:
    def play_mp4(self, filename):
        return f"Playing MP4: {filename}"

class MediaAdapter:
    def __init__(self, player, audio_type):
        self.player = player
        self.audio_type = audio_type

    def play(self, filename):
        if self.audio_type == "mp3":
            return self.player.play_mp3(filename)
        elif self.audio_type == "mp4":
            return self.player.play_mp4(filename)

class AudioPlayer:
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            return Mp3Player().play_mp3(filename)
        else:
            adapter = MediaAdapter(Mp4Player(), audio_type)
            return adapter.play(filename)

player = AudioPlayer()
print(player.play("mp3", "song.mp3"))
print(player.play("mp4", "video.mp4"))
Output:

NEW: Hello
OLD: Hello
Playing MP3: song.mp3
Playing MP4: video.mp4
Key Point: The Adapter Pattern makes incompatible interfaces work together by wrapping an existing class with a new interface. The adapter translates calls from the expected interface to the actual interface of the wrapped object. This is useful for integrating legacy code or third-party libraries without modifying existing code.

challenge
In this challenge, you will implement the Adapter design pattern to integrate legacy systems with a modern application architecture. The Adapter pattern allows objects with incompatible interfaces to work together by creating a wrapper (adapter) that translates one interface to another.



Your company has a legacy data analysis and visualization system that needs to be integrated with a new modern analytics platform. The legacy components have interfaces that are incompatible with the new system. Instead of rewriting the legacy code (which would be risky and expensive), you've been tasked with creating adapters to make these components work with the new system.

You need to:

Understand the modern interfaces defined in interfaces.py (this file cannot be modified)
Examine the legacy components in legacy_system.py (this file cannot be modified)
Implement adapter classes in adapters.py that make the legacy components compatible with the modern interfaces
Create a modern system in modern_system.py that uses these interfaces"""
