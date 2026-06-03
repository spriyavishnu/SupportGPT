import { describe, it, expect } from 'vitest';
import {
  validateEmail,
  validatePassword,
  validateLoginForm,
  formatUserRole,
} from './authUtils';

describe('authUtils', () => {
  describe('validateEmail', () => {
    it('should return true for valid email', () => {
      expect(validateEmail('test@example.com')).toBe(true);
    });

    it('should return false for invalid email', () => {
      expect(validateEmail('invalid-email')).toBe(false);
    });

    it('should return false for empty string', () => {
      expect(validateEmail('')).toBe(false);
    });
  });

  describe('validatePassword', () => {
    it('should return true for password >= 8 characters', () => {
      expect(validatePassword('password123')).toBe(true);
    });

    it('should return false for password < 8 characters', () => {
      expect(validatePassword('pass')).toBe(false);
    });
  });

  describe('validateLoginForm', () => {
    it('should return no errors for valid credentials', () => {
      const result = validateLoginForm({
        email: 'test@example.com',
        password: 'password123',
      });
      expect(result).toHaveLength(0);
    });

    it('should return error for missing email', () => {
      const result = validateLoginForm({
        email: '',
        password: 'password123',
      });
      expect(result).toContain('Email is required');
    });

    it('should return error for short password', () => {
      const result = validateLoginForm({
        email: 'test@example.com',
        password: 'pass',
      });
      expect(result).toContain('Password must be at least 8 characters');
    });
  });

  describe('formatUserRole', () => {
    it('should capitalize role correctly', () => {
      expect(formatUserRole('admin')).toBe('Admin');
      expect(formatUserRole('user')).toBe('User');
      expect(formatUserRole('ADMIN')).toBe('Admin');
    });
  });
});