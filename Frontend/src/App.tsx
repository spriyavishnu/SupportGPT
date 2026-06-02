import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { UserList } from './components/UserList';
import './App.css';

function App() {
  const mockUsers = [
    { id: 1, email: 'admin@example.com', role: 'admin' },
    { id: 2, email: 'user1@example.com', role: 'user' },
    { id: 3, email: 'user2@example.com', role: 'user' },
    { id: 4, email: 'moderator@example.com', role: 'moderator' },
  ];

  return (
    <Router>
      <div className="App" data-testid="app-container">
        <header className="App-header">
          <h1>SupportGPT - User Management</h1>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<UserList users={mockUsers} />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;