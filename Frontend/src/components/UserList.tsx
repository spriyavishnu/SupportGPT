import React, { useState } from 'react';
import { UserCard } from './UserCard';

interface User {
  id: number;
  email: string;
  role: string;
}

interface UserListProps {
  users: User[];
}

export const UserList: React.FC<UserListProps> = ({ users }) => {
  const [filterRole, setFilterRole] = useState<string>('');

  const filteredUsers = filterRole
    ? users.filter((user) => user.role === filterRole)
    : users;

  return (
    <div className="user-list" data-testid="user-list">
      <div className="filter-section">
        <label htmlFor="role-filter">Filter by Role: </label>
        <input
          id="role-filter"
          type="text"
          placeholder="e.g., admin, user"
          value={filterRole}
          onChange={(e) => setFilterRole(e.target.value)}
          data-testid="filter-input"
        />
      </div>
      <div className="users-container">
        {filteredUsers.length > 0 ? (
          filteredUsers.map((user) => (
            <UserCard
              key={user.id}
              id={user.id}
              email={user.email}
              role={user.role}
            />
          ))
        ) : (
          <p data-testid="no-users">No users found</p>
        )}
      </div>
    </div>
  );
};
