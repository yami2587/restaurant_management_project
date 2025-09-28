import time

class SessionManager:
    def __init__(self, expiry_seconds):
        """
        Initialize the session manager.
        :param expiry_seconds: Session validity duration in seconds.
        """
        self.expiry_seconds = expiry_seconds
        self.sessions = {}  # {session_id: creation_time}
    
    def create_session(self, session_id):
        """
        Create a new session with the current timestamp.
        :param session_id: Unique identifier for the session.
        """
        self.sessions[session_id] = time.time()
        return f"Session {session_id} created."

    def is_session_active(self, session_id,sliding=False):
        """
        Check if a session is active or expired.
        If expired, delete it automatically.
        :param session_id: Unique identifier for the session.
        :return: True if active, False otherwise.
        """
        if session_id not in self.sessions:
            return False
        
        created_at = self.sessions[session_id]
        if time.time() - created_at <= self.expiry_seconds:
            if sliding:
                # Refresh timestamp if session is still valid
                self.sessions[session_id] = time.time()
            return True
        else:
            # Expired → clean it up
            del self.sessions[session_id]
            return False

    def delete_session(self, session_id):
        """
        Delete a session manually (logout).
        :param session_id: Unique identifier for the session.
        :return: "Deleted" or "Not Found"
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            return "Deleted"
        return "Not Found"
