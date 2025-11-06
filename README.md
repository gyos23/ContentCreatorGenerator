# ContentCreatorGenerator

An interactive app to help generate social media content in Dorian's style and grow engagement and business.

Available in two versions:
- **Web App** - Beautiful web interface (deploy on Vercel)
- **CLI App** - Command-line interface for local use

## Quick Start

### Option 1: Web App (Recommended for Vercel)

#### Deploy to Vercel
1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com) and sign in
3. Click "New Project"
4. Import your repository
5. Vercel will auto-detect the settings
6. Click "Deploy"

Your app will be live in minutes!

#### Run Locally (Web Version)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python api/index.py

# Open browser to http://localhost:5000
```

### Option 2: CLI App (Command Line)

```bash
# Navigate to the repository
cd ContentCreatorGenerator

# Run the CLI app (Python 3.7+ required, no dependencies needed)
python3 content_generator.py
```

### Features

1. **Instagram Reel Generator** - Create full 60-second reel scripts with:
   - Problem-solution format
   - Detailed timestamps and visual cues
   - B-roll placement markers
   - Your signature style and CTAs

2. **Content Hook Generator** - Generate attention-grabbing hooks for any topic

3. **Content Framework Library** - Access proven content structures:
   - Problem-Solution Framework
   - Storytelling Framework
   - Listicle Framework

4. **Quick Content Ideas** - Get instant content ideas for rapid creation

### How to Use

1. Run `python3 content_generator.py`
2. Choose from the menu options (1-6)
3. Select your preferred category or topic
4. Get generated content in your unique style
5. Copy and customize for your platform

### Content Categories

- **Personal Growth**: Dealing with negative people, building confidence, setting boundaries, managing stress
- **Professional Development**: Leadership, communication, time management, networking
- **Mindset**: Positive thinking, emotional intelligence, self-discipline, motivation

## Your Content Style Guide

Here's an example of my style

Instagram Reel Template: Problem-Solution Format
STRUCTURE BREAKDOWN
HOOK (0-3 seconds)
[Talking Head]

Pattern: "[Common challenge/misconception]. [Counter-intuitive truth]."
Example: "Negative people. The easiest thing to do is to get rid of negative people when you don't agree with them. But the reality is that's not always an option."

CREDIBILITY STATEMENT (3-8 seconds)
[Talking Head]

Pattern: "Hi my name is [Your Name]. I'm a [day job/primary credential] and [secondary credential/mission statement]."
Example: "Hi my name is Dorian. I'm a senior project manager for a major airline by day and by night I share content with thousands of people focused on personal growth and development."

TRANSITION TO VALUE (8-12 seconds)
[Talking Head → B-roll begins]

Pattern: "[Context qualifier] here are [number] ways to [solve the problem]."
Example: "[B-roll: relevant context visuals] Whether in your community or at work [end B-roll] here are three ways to work with people you don't get along with."

TIP #1 (12-25 seconds)
[Talking Head with strategic B-roll]

Pattern: "[Number], [action-oriented tip title]. [Explanation of the tip and why it matters]."
Example: "One limit your interaction. Do what you have to do and get the job done, but you don't necessarily need to give them access to your energy."

TIP #2 (25-40 seconds)
[Talking Head with B-roll overlay]

Pattern: "[Number], [action-oriented tip title]. [B-roll: supporting visuals] [Deeper explanation with practical application] [end B-roll]."
Example: "Two, try empathizing. [B-roll] You don't have to like someone, but if you try to understand where they're coming [end B-roll] from you'd be surprised with a couple of questions coming from a genuine place how far that can take you in a relationship with someone."

TIP #3 (40-55 seconds)
[Talking Head with B-roll overlay]

Pattern: "[Number], [action-oriented tip title]. [B-roll: supporting visuals] [Explanation with boundary/implementation detail] [end B-roll]. [Empowering closing statement]."
Example: "Three, set clear boundaries. [B-roll] You have to let them know what's acceptable, what's not acceptable, [end B-roll] and then you have to personally respect your own boundaries. If they wanna live in negativity, that's cool, but you don't have to live there."

CALL TO ACTION (55-60 seconds)
[Talking Head]

Pattern: "If you found this helpful, follow along and share this with someone who might need it today. [Signature sign-off]."
Example: "If you found this helpful, follow along and share this with someone who might need it today. Let's grow together."


KEY ELEMENTS
✅ B-roll placement: Strategic use during tips 2-3 to maintain visual interest
✅ Conversational tone: Natural, like talking to a friend
✅ Actionable tips: Each one is specific and implementable
✅ Empowerment focus: Ends with audience agency/control
✅ Community building: "Let's grow together" creates connection

TIMING GUIDE

Total length: 55-60 seconds
Hook: 3-5 seconds
Intro: 5-8 seconds
Each tip: 10-15 seconds
CTA: 5 seconds


The original script:

Talking head video
Negative people. The easiest thing to do is to get rid of negative people when you don't agree with them. But the reality is that's not always an option. Hi my name is Dorian. I'm a senior project manager for a major airline by day and by night I share content with thousands of people focused on personal growth and development. [start B-roll] Whether in your community or at work [end B-roll] here are three ways to work with people you don't get along with. One limit your interaction Do what you have to do and get the job done, but you don't necessarily need to give them access to your energy. Two, try empathizing. [start B-roll] You don't have to like someone, but if you try to understand where they're coming [end B-roll] from you'd be surprised with a couple of questions coming from a genuine place how far that can take you in a relationship with someone. Three, set clear boundaries. [start B-roll] You have to let them know what's acceptable, what's not acceptable, [end B-roll] and then you have to personally respect your own boundaries. If they wanna live in negativity, that's cool, but you don't have to live there. If you found this helpful, follow along and share this with someone who might need it today. Let's grow together. [end visual]
