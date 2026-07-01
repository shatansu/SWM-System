import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Recycle, Menu, X } from 'lucide-react';
import './Navbar.css';

function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <nav className={`navbar ${scrolled ? 'navbar-scrolled' : ''}`}>
      <div className="navbar-inner">
        {/* Logo */}
        <Link to="/" className="navbar-logo">
          <div className="navbar-logo-icon">
            <Recycle size={24} />
          </div>
          <span className="navbar-logo-text">
            Eco<span className="text-gradient">Visionars</span>
          </span>
        </Link>

        {/* Desktop Nav Links */}
        <div className="navbar-links">
          <a href="#features" className="navbar-link">Features</a>
          <a href="#how-it-works" className="navbar-link">How It Works</a>
          <a href="#impact" className="navbar-link">Impact</a>
        </div>

        {/* Desktop Auth Buttons */}
        <div className="navbar-actions">
          <Link to="/login" className="btn btn-ghost">Log In</Link>
          <Link to="/register" className="btn btn-primary">Get Started</Link>
        </div>

        {/* Mobile Menu Toggle */}
        <button
          className="navbar-mobile-toggle"
          onClick={() => setMobileOpen(!mobileOpen)}
          aria-label="Toggle menu"
        >
          {mobileOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      {/* Mobile Menu */}
      <div className={`navbar-mobile-menu ${mobileOpen ? 'open' : ''}`}>
        <a href="#features" className="navbar-mobile-link" onClick={() => setMobileOpen(false)}>Features</a>
        <a href="#how-it-works" className="navbar-mobile-link" onClick={() => setMobileOpen(false)}>How It Works</a>
        <a href="#impact" className="navbar-mobile-link" onClick={() => setMobileOpen(false)}>Impact</a>
        <div className="navbar-mobile-actions">
          <Link to="/login" className="btn btn-ghost" style={{ width: '100%' }}>Log In</Link>
          <Link to="/register" className="btn btn-primary" style={{ width: '100%' }}>Get Started</Link>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
