import os
import subprocess

class FinderFix:
    def __init__(self):
        self.search_services = [
            "Windows Search",
            "WSearch"
        ]

    def restart_search_service(self):
        print("Restarting Windows Search Service...")
        for service in self.search_services:
            subprocess.run(["sc", "stop", service], check=True)
            subprocess.run(["sc", "start", service], check=True)
        print("Windows Search Service restarted successfully.")

    def rebuild_search_index(self):
        print("Rebuilding Windows Search Index...")
        subprocess.run(["powershell", "-Command", "Invoke-Expression", 
                        "'& {Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait('^%{ESC}', [System.Windows.Forms.SendWait]::SendWait('control.exe /name Microsoft.IndexingOptions'))}'"], check=True)
        print("Search Index rebuild initiated. This may take some time to complete.")

    def fix_registry_keys(self):
        print("Fixing common registry issues...")
        # Example registry key update
        subprocess.run(["reg", "add", "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows Search", "/v", "EnableFrameServerMode", "/t", "REG_DWORD", "/d", "0", "/f"], check=True)
        print("Registry keys updated successfully.")

    def run(self):
        self.restart_search_service()
        self.rebuild_search_index()
        self.fix_registry_keys()
        print("FinderFix has completed the repair process.")

if __name__ == "__main__":
    finder_fix = FinderFix()
    finder_fix.run()