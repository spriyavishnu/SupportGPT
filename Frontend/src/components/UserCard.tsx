import React from 'react';

interface UserCardProps {
  id: number;
  email: string;
  role: string;
}

export const UserCard: React.FC<UserCardProps> = ({ id, email, role }) => {
  return (
    <div className="user-card" data-testid="user-card">
      <h3 data-testid="user-email">{email}</h3>
      <p data-testid="user-role">Role: {role}</p>
      <p data-testid="user-id">ID: {id}</p>
    </div>
  );
};
