import { Link } from 'react-router-dom';
import {
  Camera,
  MapPin,
  Truck,
  Recycle,
  Shield,
  BarChart3,
  ArrowRight,
  Scan,
  CheckCircle2,
  Navigation,
  Leaf,
  Globe,
  Users,
  Zap,
  ChevronRight,
  Sparkles
} from 'lucide-react';
import Navbar from '../components/Navbar';
import './Landing.css';

function Landing() {
  const features = [
    {
      icon: <Camera size={28} />,
      title: 'AI Waste Scanner',
      description: 'Take a photo of waste and our Gemini AI instantly classifies it — plastic, organic, metal, and more.',
      color: '#10B981'
    },
    {
      icon: <Navigation size={28} />,
      title: 'Live Tracking',
      description: 'Track your waste collector in real-time on a map, just like tracking a delivery order.',
      color: '#8B5CF6'
    },
    {
      icon: <Truck size={28} />,
      title: 'Smart Pickup',
      description: 'Request waste pickup at your location. Nearby collectors get notified and accept instantly.',
      color: '#3B82F6'
    },
    {
      icon: <Shield size={28} />,
      title: 'Verified Collectors',
      description: 'All waste collectors are verified with role-based access. Accept, track, and complete pickups securely.',
      color: '#F59E0B'
    },
    {
      icon: <Recycle size={28} />,
      title: 'Disposal Guidance',
      description: 'Get AI-powered disposal instructions for every waste type. Know exactly where and how to dispose.',
      color: '#EF4444'
    },
    {
      icon: <BarChart3 size={28} />,
      title: 'Impact Dashboard',
      description: 'See your environmental impact — waste diverted from landfills, carbon saved, and community stats.',
      color: '#06B6D4'
    }
  ];

  const steps = [
    {
      step: '01',
      icon: <Scan size={32} />,
      title: 'Scan Waste',
      description: 'Open the app, point your camera at waste, and let AI identify what type of waste it is.'
    },
    {
      step: '02',
      icon: <MapPin size={32} />,
      title: 'Request Pickup',
      description: 'Your GPS location is captured automatically. Submit the report and a nearby collector is notified.'
    },
    {
      step: '03',
      icon: <CheckCircle2 size={32} />,
      title: 'Track & Complete',
      description: 'Track the collector on a live map as they arrive. Get notified when the pickup is completed.'
    }
  ];

  const stats = [
    { value: '10K+', label: 'Waste Reports', icon: <Camera size={20} /> },
    { value: '2.5K+', label: 'Pickups Done', icon: <Truck size={20} /> },
    { value: '500+', label: 'Active Collectors', icon: <Users size={20} /> },
    { value: '15T', label: 'Waste Diverted', icon: <Leaf size={20} /> }
  ];

  return (
    <div className="landing">
      <Navbar />

      {/* ── Hero Section ── */}
      <section className="hero">
        <div className="hero-bg">
          <div className="hero-orb hero-orb-1"></div>
          <div className="hero-orb hero-orb-2"></div>
          <div className="hero-orb hero-orb-3"></div>
          <div className="hero-grid"></div>
        </div>

        <div className="container hero-content">
          <div className="hero-badge animate-fade-in-down">
            <Sparkles size={14} />
            <span>Powered by Gemini AI</span>
          </div>

          <h1 className="hero-title animate-fade-in-up delay-1">
            Smart Waste Management
            <br />
            <span className="text-gradient">For a Cleaner Future</span>
          </h1>

          <p className="hero-subtitle animate-fade-in-up delay-2">
            Scan waste with AI, request instant pickups, and track collectors in real-time. 
            Join thousands making their city cleaner, one scan at a time.
          </p>

          <div className="hero-actions animate-fade-in-up delay-3">
            <Link to="/register" className="btn btn-primary btn-lg">
              Start Scanning
              <ArrowRight size={18} />
            </Link>
            <a href="#how-it-works" className="btn btn-outline btn-lg">
              See How It Works
            </a>
          </div>

          <div className="hero-stats animate-fade-in-up delay-4">
            {stats.map((stat, index) => (
              <div key={index} className="hero-stat">
                <div className="hero-stat-icon">{stat.icon}</div>
                <div>
                  <div className="hero-stat-value">{stat.value}</div>
                  <div className="hero-stat-label">{stat.label}</div>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="hero-scroll-indicator animate-fade-in delay-5">
          <div className="scroll-line"></div>
        </div>
      </section>

      {/* ── Features Section ── */}
      <section className="section features-section" id="features">
        <div className="container">
          <div className="section-header">
            <div className="section-label">
              <Zap size={14} />
              <span>Features</span>
            </div>
            <h2>Everything You Need to <span className="text-gradient">Fight Waste</span></h2>
            <p>From AI scanning to live tracking — a complete waste management ecosystem powered by cutting-edge technology.</p>
          </div>

          <div className="features-grid">
            {features.map((feature, index) => (
              <div key={index} className="feature-card card" style={{ '--accent': feature.color }}>
                <div className="feature-icon" style={{ background: `${feature.color}15`, color: feature.color }}>
                  {feature.icon}
                </div>
                <h3 className="feature-title">{feature.title}</h3>
                <p className="feature-desc">{feature.description}</p>
                <div className="feature-arrow">
                  <ChevronRight size={16} />
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── How It Works Section ── */}
      <section className="section how-section" id="how-it-works">
        <div className="container">
          <div className="section-header">
            <div className="section-label">
              <Globe size={14} />
              <span>How It Works</span>
            </div>
            <h2>Three Simple Steps to a <span className="text-gradient">Cleaner City</span></h2>
            <p>Getting started takes less than a minute. Scan, report, and let the system handle the rest.</p>
          </div>

          <div className="steps-grid">
            {steps.map((step, index) => (
              <div key={index} className="step-card">
                <div className="step-number">{step.step}</div>
                <div className="step-icon-wrap">
                  {step.icon}
                </div>
                <h3 className="step-title">{step.title}</h3>
                <p className="step-desc">{step.description}</p>
                {index < steps.length - 1 && (
                  <div className="step-connector">
                    <ArrowRight size={20} />
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── Impact / CTA Section ── */}
      <section className="section cta-section" id="impact">
        <div className="container">
          <div className="cta-card">
            <div className="cta-bg-effects">
              <div className="cta-orb cta-orb-1"></div>
              <div className="cta-orb cta-orb-2"></div>
            </div>
            <div className="cta-content">
              <h2>Ready to Make an <span className="text-gradient">Impact</span>?</h2>
              <p>
                Join the Eco Visionars community. Every waste scan, every pickup request — 
                you're building a cleaner, greener future for your city.
              </p>
              <div className="cta-actions">
                <Link to="/register" className="btn btn-primary btn-lg">
                  Join as Citizen
                  <ArrowRight size={18} />
                </Link>
                <Link to="/register" className="btn btn-outline btn-lg">
                  Become a Collector
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ── Footer ── */}
      <footer className="footer">
        <div className="container">
          <div className="footer-content">
            <div className="footer-brand">
              <div className="navbar-logo">
                <div className="navbar-logo-icon">
                  <Recycle size={20} />
                </div>
                <span className="navbar-logo-text">
                  Eco<span className="text-gradient">Visionars</span>
                </span>
              </div>
              <p className="footer-tagline">
                AI-powered waste management platform built for Global Buildathon'26.
              </p>
            </div>

            <div className="footer-links-group">
              <h4>Product</h4>
              <a href="#features">Features</a>
              <a href="#how-it-works">How It Works</a>
              <a href="#impact">Impact</a>
            </div>

            <div className="footer-links-group">
              <h4>Roles</h4>
              <Link to="/register">Citizen</Link>
              <Link to="/register">Collector</Link>
              <Link to="/register">Admin</Link>
            </div>

            <div className="footer-links-group">
              <h4>Team</h4>
              <span>Serina Bernard</span>
              <span>Shatansu Kurmi</span>
              <span>Aman & Saniya</span>
            </div>
          </div>

          <div className="footer-bottom">
            <p>&copy; 2026 Eco Visionars. Built with 💚 for Global Buildathon'26.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default Landing;
