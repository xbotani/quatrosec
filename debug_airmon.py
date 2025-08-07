#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import re
import sys

def run_command(cmd):
    """Run a command and return stdout, stderr, and return code"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), -1

def test_airmon_ng():
    """Test airmon-ng output parsing"""
    print("=== Testing airmon-ng ===")
    
    # Test airmon-ng without arguments
    stdout, stderr, returncode = run_command("airmon-ng")
    print(f"airmon-ng return code: {returncode}")
    print("STDOUT:")
    print(stdout)
    print("STDERR:")
    print(stderr)
    
    # Test airmon-ng check
    stdout, stderr, returncode = run_command("airmon-ng check")
    print(f"\nairmon-ng check return code: {returncode}")
    print("STDOUT:")
    print(stdout)
    print("STDERR:")
    print(stderr)

def test_iwconfig():
    """Test iwconfig output"""
    print("\n=== Testing iwconfig ===")
    
    stdout, stderr, returncode = run_command("iwconfig")
    print(f"iwconfig return code: {returncode}")
    print("STDOUT:")
    print(stdout)
    print("STDERR:")
    print(stderr)

def test_ifconfig():
    """Test ifconfig output"""
    print("\n=== Testing ifconfig ===")
    
    stdout, stderr, returncode = run_command("ifconfig")
    print(f"ifconfig return code: {returncode}")
    print("STDOUT:")
    print(stdout)
    print("STDERR:")
    print(stderr)

def test_interface_detection():
    """Test interface detection"""
    print("\n=== Testing interface detection ===")
    
    # Get wireless interfaces
    stdout, stderr, returncode = run_command("iwconfig")
    interfaces = []
    current_interface = None
    
    for line in stdout.split('\n'):
        if line.strip() and not line.startswith(' '):
            # This is an interface line
            parts = line.split()
            if parts:
                current_interface = parts[0]
                interfaces.append(current_interface)
        elif line.strip() and 'Mode:' in line and current_interface:
            # This line contains mode information
            print(f"Interface: {current_interface}, Line: {line.strip()}")
    
    print(f"Found interfaces: {interfaces}")

def test_airmon_start():
    """Test airmon-ng start on first wireless interface"""
    print("\n=== Testing airmon-ng start ===")
    
    # Get first wireless interface
    stdout, stderr, returncode = run_command("iwconfig")
    interfaces = []
    
    for line in stdout.split('\n'):
        if line.strip() and not line.startswith(' '):
            parts = line.split()
            if parts:
                interfaces.append(parts[0])
    
    if interfaces:
        test_interface = interfaces[0]
        print(f"Testing with interface: {test_interface}")
        
        # Test airmon-ng start
        stdout, stderr, returncode = run_command(f"airmon-ng start {test_interface}")
        print(f"airmon-ng start return code: {returncode}")
        print("STDOUT:")
        print(stdout)
        print("STDERR:")
        print(stderr)
        
        # Test parsing with our regex patterns
        patterns = [
            r'.*\(mac80211 monitor mode (?:vif )?enabled (?:for [^ ]+ )?on (?:\[\w+\])?(\w+)\)?.*',
            r'.*\(mac80211 monitor mode (?:vif )?enabled on (?:\[\w+\])?(\w+)\)?.*',
            r'(\w+).*\(monitor mode enabled\)',
            r'(\w+).*\(monitor mode\)',
            r'(\w+mon)',
        ]
        
        print("\nTesting regex patterns:")
        for i, pattern in enumerate(patterns):
            for line in stdout.split('\n'):
                matches = re.match(pattern, line)
                if matches:
                    print(f"Pattern {i+1} matched: {matches.group(1)}")
                    break
    else:
        print("No wireless interfaces found")

if __name__ == "__main__":
    test_airmon_ng()
    test_iwconfig()
    test_ifconfig()
    test_interface_detection()
    test_airmon_start()
