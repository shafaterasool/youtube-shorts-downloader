#!/usr/bin/env python3
"""
YouTube Shorts Channel Downloader
Owner permission required - ye script sirf authorized downloads ke liye hai
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
        print("✅ yt-dlp successfully installed!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Installation failed. Please install manually:")
        print("   pip install -U yt-dlp")
        return False

def download_channel_shorts(channel_url, output_folder="./youtube_shorts"):
    """
    YouTube channel se sab shorts download karo
    
    Args:
        channel_url: YouTube channel ka URL (jaise @channelname ya full URL)
        output_folder: Jahan save karni hai shorts
    """
    
    # Check yt-dlp
    if not check_yt_dlp_installed():
        print("yt-dlp installed nahi hai, installing...")
        if not install_yt_dlp():
            return False
    
    # Output folder create karo
    os.makedirs(output_folder, exist_ok=True)
    
    # Timestamp add karo folder mein
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    final_folder = os.path.join(output_folder, f"downloads_{timestamp}")
    os.makedirs(final_folder, exist_ok=True)
    
    print(f"\n🎬 YouTube Shorts Download ho rahe hain...")
    print(f"📍 Channel: {channel_url}")
    print(f"💾 Save location: {final_folder}")
    print("-" * 50)
    
    # yt-dlp command - simplified for compatibility
    # Directly access /shorts endpoint for channel shorts
    shorts_url = channel_url.rstrip('/') + '/shorts'
    
    command = [
        sys.executable,
        '-m', 'yt_dlp',
        shorts_url,
        '-o', os.path.join(final_folder, '%(title)s.%(ext)s'),
        '--format', 'best',
        '-N', '4',  # 4 parallel downloads
    ]
    
    try:
        print("\n⏳ Download start ho raha hai...\n")
        subprocess.run(command, check=True)
        print("\n" + "=" * 50)
        print("✅ Download complete!")
        print(f"📂 Files saved in: {final_folder}")
        print("=" * 50)
        
        # Auto-open folder
        print("\n🔓 Folder open ho raha hai...\n")
        try:
            if sys.platform == 'win32':
                # Windows
                os.startfile(final_folder)
            elif sys.platform == 'darwin':
                # Mac
                subprocess.run(['open', final_folder])
            else:
                # Linux
                subprocess.run(['xdg-open', final_folder])
        except Exception as e:
            print(f"⚠️  Folder auto-open nahi hua: {e}")
            print(f"📂 Manual open karo: {final_folder}")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Download mein error: {e}")
        return False
    except KeyboardInterrupt:
        print("\n⚠️  Download cancel kiya gaya")
        return False

def main():
    print("""
╔════════════════════════════════════════╗
║  YouTube Shorts Channel Downloader     ║
║  Owner Permission Required             ║
╚════════════════════════════════════════╝
    """)
    
    # Channel URL lo
    channel_url = input("\n📝 YouTube Channel URL (ya @channelname) daalen:\n> ").strip()
    
    if not channel_url:
        print("❌ URL khali hai!")
        return
    
    # Output folder
    output_folder = input("\n💾 Download folder (default: ./youtube_shorts):\n> ").strip()
    if not output_folder:
        output_folder = "./youtube_shorts"
    
    # Confirmation
    print(f"\n✓ Channel: {channel_url}")
    print(f"✓ Folder: {output_folder}")
    confirm = input("\nKya thik hai? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("Cancelled")
        return
    
    # Download start
    success = download_channel_shorts(channel_url, output_folder)
    
    if success:
        print(f"\n🎉 Sab kuch complete! Shorts {output_folder} mein hain")
    else:
        print(f"\n⚠️  Kuch masla hua. Dobaara try karen")

if __name__ == "__main__":
    main()
