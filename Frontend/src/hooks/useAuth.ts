import { useState } from 'react';

interface AuthState {
  isAuthenticated: boolean;
  user: { email: string; role: string } | null;
  loading: boolean;
}

export const useAuth = () => {
  const [authState, setAuthState] = useState<AuthState>({
    isAuthenticated: false,
    user: null,
    loading: false,
  });

  const login = (email: string, role: string) => {
    setAuthState({
      isAuthenticated: true,
      user: { email, role },
      loading: false,
    });
  };

  const logout = () => {
    setAuthState({
      isAuthenticated: false,
      user: null,
      loading: false,
    });
  };

  return {
    ...authState,
    login,
    logout,
  };
};
