#!/usr/bin/env python3
"""
YouTube Shorts Channel Downloader - FIXED VERSION
Owner permission required - authorized downloads ke liye
"""

import os
import sys
import subprocess
from datetime import datetime

def check_yt_dlp_installed():
    """Check agar yt-dlp installed hai"""
    try:
        subprocess.run([sys.executable, '-m', 'yt_dlp', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_yt_dlp():
    """yt-dlp install karo"""
    print("📦 yt-dlp install ho raha hai...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp'], check=True)
        print("✅ yt-dlp installed!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Installation failed")
        return False

def download_channel_shorts(channel_url, output_folder="./youtube_shorts"):
    """
    YouTube channel se sab shorts download karo
    """
    
    # Check yt-dlp
    if not check_yt_dlp_installed():
        print("yt-dlp installing...")
        if not install_yt_dlp():
            return False
    
    # Output folder
    os.makedirs(output_folder, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    final_folder = os.path.join(output_folder, f"downloads_{timestamp}")
    os.makedirs(final_folder, exist_ok=True)
    
    print(f"\n🎬 YouTube Shorts Download...")
    print(f"📍 Channel: {channel_url}")
    print(f"💾 Location: {final_folder}")
    print("-" * 60)
    
    # YouTube shorts URL
    shorts_url = channel_url.rstrip('/') + '/shorts'
    
    # FIXED: Add unique ID to filename (simple & compatible)
    command = [
        sys.executable,
        '-m', 'yt_dlp',
        shorts_url,
        '-o', os.path.join(final_folder, '%(title)s_%(id)s.%(ext)s'),  # ID prevents duplicates
        '--format', 'best',
        '-N', '4',
        '--ignore-errors',  # Continue even if one fails
    ]
    
    try:
        print("\n⏳ Downloading...\n")
        subprocess.run(command, check=False)  # Don't fail on errors
        
        print("\n" + "=" * 60)
        print("✅ Download complete!")
        print(f"📂 Location: {final_folder}")
        print("=" * 60)
        
        # Auto-open folder
        print("\n🔓 Opening folder...\n")
        try:
            if sys.platform == 'win32':
                os.startfile(final_folder)
            elif sys.platform == 'darwin':
                subprocess.run(['open', final_folder])
            else:
                subprocess.run(['xdg-open', final_folder])
        except Exception as e:
            print(f"Folder: {final_folder}")
        
        return True
        
    except KeyboardInterrupt:
        print("\n⚠️  Cancelled")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

def main():
    print("""
╔════════════════════════════════════════╗
║  YouTube Shorts Downloader (FIXED)     ║
║  Owner Permission Required             ║
╚════════════════════════════════════════╝
    """)
    
    channel_url = input("\n📝 YouTube Channel URL:\n> ").strip()
    
    if not channel_url:
        print("❌ URL required!")
        return
    
    output_folder = input("\n💾 Folder (default: ./youtube_shorts):\n> ").strip()
    if not output_folder:
        output_folder = "./youtube_shorts"
    
    print(f"\n{'='*60}")
    print(f"Channel: {channel_url}")
    print(f"Folder: {output_folder}")
    print(f"{'='*60}")
    
    confirm = input("\nStart? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("Cancelled")
        return
    
    download_channel_shorts(channel_url, output_folder)

if __name__ == "__main__":
    main()
