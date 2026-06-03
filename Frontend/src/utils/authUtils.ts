export interface LoginCredentials {
  email: string;
  password: string;
}

export const validateEmail = (email: string): boolean => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

export const validatePassword = (password: string): boolean => {
  return password.length >= 8;
};

export const validateLoginForm = (credentials: LoginCredentials): string[] => {
  const errors: string[] = [];

  if (!credentials.email) {
    errors.push('Email is required');
  } else if (!validateEmail(credentials.email)) {
    errors.push('Invalid email format');
  }

  if (!credentials.password) {
    errors.push('Password is required');
  } else if (!validatePassword(credentials.password)) {
    errors.push('Password must be at least 8 characters');
  }

  return errors;
};

export const formatUserRole = (role: string): string => {
  return role.charAt(0).toUpperCase() + role.slice(1).toLowerCase();
};
