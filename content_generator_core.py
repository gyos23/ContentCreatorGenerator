#!/usr/bin/env python3
"""
Social Media Content Generator
Generates engaging content ideas in your unique style to grow engagement and business.
Now with 101 hook templates, 20+ messaging frameworks, and creative variety!
"""

import random
import json
from typing import Dict, List
from datetime import datetime


class StyleGuide:
    """Contains Dorian's content style patterns and voice"""

    def __init__(self):
        self.name = "Dorian"
        self.credentials = {
            "day_job": "senior project manager for a major airline",
            "mission": "share content with thousands of people focused on personal growth and development"
        }
        self.signature_cta = "If you found this helpful, follow along and share this with someone who might need it today. Let's grow together."
        self.tone = "straightforward, no-BS, strategic, empathetic when necessary, hip hop authenticity"

    def get_intro(self) -> str:
        """Generate credibility statement with variations"""
        intros = [
            f"Hi my name is {self.name}. I'm a {self.credentials['day_job']} by day and by night I {self.credentials['mission']}.",
            f"I'm {self.name}. {self.credentials['day_job']} by day, helping people grow by night.",
            f"I'm {self.name}, a {self.credentials['day_job']}. I {self.credentials['mission']}.",
        ]
        return random.choice(intros)

    def get_cta(self, content_type: str = "standard") -> str:
        """Generate CTA with variations based on content type"""
        ctas = {
            "standard": self.signature_cta,
            "share": "If this resonated with you, share it with someone who needs to hear it. Let's grow together.",
            "follow": "Follow along for more real talk on growth and leadership. Let's grow together.",
            "planner": f"{self.signature_cta.split('.')[0]}. Check out my planners in the link to take your growth to the next level.",
            "clients": "If you're ready to level up your leadership or personal growth, let's connect. Link in bio. Let's grow together.",
            "comment": "Drop a comment and let me know - which one hit different for you? Let's grow together.",
        }

        # Mostly return standard, sometimes vary
        if random.random() < 0.15:  # 15% chance to vary
            return random.choice(list(ctas.values()))
        return ctas.get(content_type, self.signature_cta)


class HookLibrary:
    """Library of 101 hook templates from Creator Blueprints"""

    HOOK_TEMPLATES = [
        # Direct Question Hooks
        "Want to {desired_result} but don't want to {thing_they_dont_want}? Try this.",
        "Want to {desired_result} without {thing_they_dont_want}? Here's how.",
        "Trying to {desired_result}? Stop doing {common_mistake}.",
        "Struggling with {problem}? Here's what's really holding you back.",

        # Pattern Interrupt Hooks
        "Here's why most {target_audience} fail to {desired_result}",
        "The #1 reason {target_audience} struggle with {problem}",
        "This is what nobody tells you about {topic}",
        "The truth about {topic} that most people miss",

        # Controversial/Bold Claims
        "Unpopular opinion: {controversial_take}",
        "{common_belief} is actually making things worse",
        "Stop {common_advice}. Do this instead.",
        "I used to believe {old_belief}. I was wrong.",

        # Story-Based Hooks
        "I learned this the hard way: {lesson}",
        "Here's what changed everything for me about {topic}",
        "The moment I realized {insight}",
        "3 years ago, I {past_situation}. Today, {current_situation}.",

        # Problem-Focused Hooks
        "If you're {struggling_with}, you're not alone. Here's why.",
        "{problem} is costing you more than you think",
        "The biggest mistake I see with {topic}",
        "{problem}? Most people do this. Big mistake.",

        # List/Number Hooks
        "{number} signs you're {situation}",
        "{number} things I wish I knew about {topic}",
        "{number} ways to {desired_result} (the last one changed everything)",
        "Here are {number} things successful people do differently",

        # Curiosity Gaps
        "The one thing that separates {successful_group} from everyone else",
        "What {successful_person} won't tell you about {topic}",
        "The secret to {desired_result} (it's not what you think)",
        "I tried {number} different approaches to {topic}. Only one worked.",

        # Relatability Hooks
        "Can we normalize {relatable_struggle}?",
        "Is it just me or is {common_situation} getting worse?",
        "Tell me I'm not the only one who {relatable_behavior}",
        "Raise your hand if you've ever {relatable_situation}",

        # Mistake/Failure Hooks
        "I wasted {time_period} doing {mistake}. Don't make the same mistake.",
        "Here's what I got wrong about {topic}",
        "The {number} mistakes keeping you from {desired_result}",
        "I used to {old_behavior}. Then I learned this.",

        # Transformation Hooks
        "How I went from {before_state} to {after_state}",
        "Before vs After: What changed when I {action}",
        "The simple shift that transformed my {area_of_life}",
        "{time_period} ago I couldn't {struggle}. Now I {achievement}.",

        # Objection Handling
        "Think you need {perceived_requirement} to {desired_result}? Think again.",
        "You don't need {common_solution} to {desired_result}",
        "No {resource}, no problem. Here's how to {desired_result}",
        "{excuse} is not stopping you. This is.",

        # Authority/Credibility
        "After {number} years of {experience}, here's what I've learned",
        "I've helped {number} people with {problem}. This is what works.",
        "From my {number} years as a {profession}, here's the truth",
        "In my career as a {profession}, I've seen {observation}",

        # Comparison Hooks
        "{topic} vs {alternative}: Which one actually works?",
        "The difference between {approach_a} and {approach_b}",
        "Why {solution_a} beats {solution_b} every time",
        "Everyone's doing {popular_thing}. I'm doing this instead.",

        # Warning/Caution Hooks
        "If you're planning to {action}, read this first",
        "Before you {action}, you need to know this",
        "Don't {action} until you {prerequisite}",
        "This mistake with {topic} could cost you everything",

        # Myth-Busting
        "The myth about {topic} that's holding you back",
        "Let's debunk the biggest lie about {topic}",
        "Everything you think you know about {topic}? Wrong.",
        "The {topic} myth that needs to die",

        # Personal Confession
        "I'll be honest: I struggled with {problem} for years",
        "Can I be real with you about {topic}?",
        "Here's something I never talk about: {vulnerable_topic}",
        "The truth I wish someone told me about {topic}",

        # Challenge/Dare
        "Try this {action} for {time_period} and watch what happens",
        "I challenge you to {action}",
        "What would happen if you {hypothetical_action}?",
        "Here's an experiment: {challenge}",

        # Pain Point Amplification
        "Tired of {frustration}? You're doing this wrong.",
        "Still {struggling}? This is why.",
        "Fed up with {problem}? There's a better way.",
        "{frustration} doesn't have to be your reality",

        # Social Proof
        "This helped {number} people {achieve_result}",
        "Why everyone's talking about {topic}",
        "The strategy that {successful_group} use",
        "What the top {percentage}% do differently",

        # Future Pacing
        "Imagine if you could {desired_outcome}",
        "What if I told you {desired_result} was possible in {timeframe}?",
        "Picture this: {ideal_scenario}",
        "In {timeframe}, you could {achievement}. Here's how.",

        # Contrarian
        "Forget everything you know about {topic}",
        "What if {common_belief} is backwards?",
        "The opposite of {common_advice} actually works better",
        "{conventional_wisdom} is outdated. Try this.",

        # Behind the Scenes
        "Here's what really happens when {situation}",
        "The behind-the-scenes truth about {topic}",
        "What they don't show you about {topic}",
        "The reality of {topic} (unfiltered)",

        # Urgency/Timing
        "Now is the time to {action}. Here's why.",
        "If you don't {action} now, {negative_consequence}",
        "The window for {opportunity} is closing",
        "Why {current_moment} is perfect for {action}",

        # Simplification
        "{topic} doesn't have to be complicated",
        "The simple truth about {topic}",
        "How to {desired_result} in {number} simple steps",
        "I simplified {topic} down to this",

        # Recognition/Validation
        "Shoutout to everyone who {struggle}",
        "This one's for the people who {situation}",
        "To anyone who's ever {experience}: I see you",
        "If you've been {struggling}, this is your sign",

        # Stakes/Consequence
        "What's at stake if you ignore {problem}",
        "The cost of not addressing {issue}",
        "Here's what you're losing by {inaction}",
        "{problem} has bigger consequences than you think",

        # Process Reveal
        "My exact process for {desired_result}",
        "The step-by-step breakdown of {achievement}",
        "Here's my framework for {topic}",
        "The system I use to {desired_result}",
    ]

    @classmethod
    def get_hook(cls, topic: str, context: Dict = None) -> str:
        """Get a random hook template and fill it with topic-specific content"""
        template = random.choice(cls.HOOK_TEMPLATES)

        # Default context
        default_context = {
            'desired_result': f"master {topic}",
            'thing_they_dont_want': "spend years struggling",
            'common_mistake': "the same old approach",
            'problem': topic,
            'target_audience': "people",
            'topic': topic,
            'controversial_take': f"{topic} is misunderstood",
            'common_belief': f"traditional advice about {topic}",
            'common_advice': "what everyone else says",
            'old_belief': f"{topic} was impossible",
            'lesson': f"how to approach {topic}",
            'insight': f"the real key to {topic}",
            'past_situation': f"struggled with {topic}",
            'current_situation': f"I've mastered {topic}",
            'struggling_with': f"dealing with {topic}",
            'number': random.choice(['3', '4', '5', '7']),
            'situation': f"facing {topic}",
            'successful_group': "high performers",
            'successful_person': "experts",
            'relatable_struggle': f"struggling with {topic}",
            'common_situation': topic,
            'relatable_behavior': f"struggled with {topic}",
            'relatable_situation': f"dealt with {topic}",
            'time_period': random.choice(['years', 'months', '6 months', 'too long']),
            'mistake': f"the wrong approach to {topic}",
            'old_behavior': f"avoid {topic}",
            'action': f"tackle {topic}",
            'before_state': f"struggling with {topic}",
            'after_state': f"mastering {topic}",
            'area_of_life': topic,
            'achievement': f"handle it with ease",
            'perceived_requirement': random.choice(['years of experience', 'special skills', 'perfect conditions']),
            'common_solution': "the traditional approach",
            'resource': random.choice(['time', 'money', 'experience']),
            'excuse': random.choice(['Time', 'Money', 'Experience']),
            'experience': random.choice(['managing people', 'leadership', 'personal development']),
            'profession': "senior project manager",
            'observation': f"what really works with {topic}",
            'alternative': "the old way",
            'approach_a': "this method",
            'approach_b': "traditional advice",
            'solution_a': "this approach",
            'solution_b': "what everyone else does",
            'popular_thing': "the common approach",
            'prerequisite': "understand this",
            'vulnerable_topic': f"my journey with {topic}",
            'hypothetical_action': f"approached {topic} differently",
            'challenge': f"try this with {topic}",
            'frustration': f"dealing with {topic}",
            'achieve_result': f"improve their {topic}",
            'percentage': random.choice(['1', '5', '10']),
            'desired_outcome': f"finally master {topic}",
            'timeframe': random.choice(['30 days', '3 months', '90 days', 'a year']),
            'ideal_scenario': f"you've conquered {topic}",
            'conventional_wisdom': f"old advice about {topic}",
            'opportunity': f"growth in {topic}",
            'current_moment': "right now",
            'negative_consequence': "you'll keep struggling",
            'struggle': f"deal with {topic}",
            'experience': f"faced {topic}",
            'issue': topic,
            'inaction': f"not addressing {topic}",
        }

        # Merge with provided context
        if context:
            default_context.update(context)

        # Fill template
        try:
            return template.format(**default_context)
        except KeyError:
            # If template has keys we don't have, return a simpler version
            return f"Here's what you need to know about {topic}"


class MessagingFrameworks:
    """20+ messaging frameworks for content variety"""

    FRAMEWORKS = {
        "natural_law_metaphor": {
            "name": "Natural Law Metaphor",
            "structure": [
                "Hook: Present a natural law or phenomenon",
                "Bridge: Connect it to personal/professional growth",
                "Application: How this applies to your audience's life",
                "Action: What they should do with this insight"
            ]
        },
        "common_unseen_mistake": {
            "name": "Common Unseen Mistake",
            "structure": [
                "Hook: Most people do [X]",
                "Problem: But they're missing [Y]",
                "Why: Here's what's really happening",
                "Solution: Do this instead",
                "Result: What changes when you fix it"
            ]
        },
        "brutal_honesty": {
            "name": "Brutal Honesty Callout",
            "structure": [
                "Hook: Call out the hard truth",
                "Reality: No sugar-coating",
                "Why it matters: The cost of denial",
                "Path forward: What to do about it"
            ]
        },
        "cost_of_inaction": {
            "name": "Cost of Inaction",
            "structure": [
                "Hook: Present the status quo",
                "Hidden costs: What's being lost",
                "Compound effect: How it gets worse over time",
                "Alternative: What action creates"
            ]
        },
        "best_of_both_worlds": {
            "name": "Best of Both Worlds",
            "structure": [
                "Hook: The false choice",
                "Option A: Traditional path",
                "Option B: Alternative path",
                "Option C: The hybrid approach",
                "Why it works: Benefits of both"
            ]
        },
        "deeper_problem": {
            "name": "The Deeper Problem",
            "structure": [
                "Hook: Surface problem everyone sees",
                "Dig deeper: What's really causing it",
                "Root cause: The actual issue",
                "Real solution: Address the root"
            ]
        },
        "i_used_to_believe": {
            "name": "I Used To Believe",
            "structure": [
                "Hook: Old belief",
                "Experience: What changed",
                "Realization: New understanding",
                "Application: How to shift perspective"
            ]
        },
        "point_of_high_drama": {
            "name": "Point of High Drama",
            "structure": [
                "Hook: The critical moment",
                "Stakes: What was on the line",
                "Decision: What happened",
                "Lesson: What it taught",
                "Application: How you can use this"
            ]
        },
        "linear_roadmap": {
            "name": "Linear Roadmap",
            "structure": [
                "Hook: Where you want to go",
                "Step 1: First action",
                "Step 2: Next move",
                "Step 3: Final step",
                "Destination: What success looks like"
            ]
        },
        "calling_out_enemy": {
            "name": "Calling Out The Enemy",
            "structure": [
                "Hook: Name the enemy",
                "Impact: How it's hurting people",
                "Why it persists: The system keeping it alive",
                "Fight back: How to resist",
                "Victory: What winning looks like"
            ]
        },
        "great_paradox": {
            "name": "The Great Paradox",
            "structure": [
                "Hook: The contradiction",
                "Side A: One truth",
                "Side B: Opposite truth",
                "Resolution: How both are true",
                "Wisdom: Living with paradox"
            ]
        },
        "unlikely_hero": {
            "name": "The Unlikely Hero",
            "structure": [
                "Hook: The underdog",
                "Disadvantage: What was against them",
                "Secret strength: Hidden advantage",
                "Victory: How they won",
                "Lesson: What this teaches us"
            ]
        },
        "the_reporter": {
            "name": "The Reporter",
            "structure": [
                "Hook: The observation",
                "Data: What you're seeing",
                "Analysis: What it means",
                "Implications: Why it matters",
                "Forecast: What's coming"
            ]
        },
        "controversial_perspective": {
            "name": "Controversial Perspective",
            "structure": [
                "Hook: The unpopular opinion",
                "Common view: What most believe",
                "Counter-argument: Why they're wrong",
                "Evidence: Supporting your view",
                "Conclusion: Stand by your position"
            ]
        },
        "vulnerable_admission": {
            "name": "Vulnerable Admission",
            "structure": [
                "Hook: The confession",
                "Struggle: What you faced",
                "Shame: How it felt",
                "Growth: What you learned",
                "Freedom: Sharing helps others"
            ]
        },
    }

    @classmethod
    def get_random_framework(cls) -> Dict:
        """Get a random messaging framework"""
        return random.choice(list(cls.FRAMEWORKS.values()))

    @classmethod
    def get_framework(cls, framework_name: str) -> Dict:
        """Get a specific framework"""
        return cls.FRAMEWORKS.get(framework_name, cls.get_random_framework())


class HookPoints:
    """10 Hook Point techniques for attention-grabbing openings"""

    TECHNIQUES = {
        "future_pacing": {
            "name": "Future Pacing",
            "description": "Paint a picture of the desired future",
            "templates": [
                "Imagine waking up every day {positive_outcome}",
                "Picture yourself {ideal_scenario}",
                "What if {timeframe} from now, you {achievement}?",
                "Envision a life where {desired_state}"
            ]
        },
        "unresolved_problems": {
            "name": "Unresolved Problems",
            "description": "Address ongoing struggles",
            "templates": [
                "Still struggling with {problem}? Here's why.",
                "Can't seem to {desired_result}? This is the missing piece.",
                "Tired of {frustration}? There's a reason.",
                "{problem} won't go away until you {action}"
            ]
        },
        "situational_relatability": {
            "name": "Situational Relatability",
            "description": "Create instant connection",
            "templates": [
                "Ever feel like {relatable_feeling}?",
                "You know that moment when {relatable_situation}?",
                "We've all been there: {common_experience}",
                "Raise your hand if {relatable_struggle}"
            ]
        },
        "context_framing": {
            "name": "Context Framing",
            "description": "Set the stage with context",
            "templates": [
                "Here's something they don't teach you about {topic}",
                "The thing about {topic} that nobody talks about",
                "In all my years {experience}, I've learned {lesson}",
                "After {credential}, here's what I know about {topic}"
            ]
        },
        "stories": {
            "name": "Stories",
            "description": "Draw people in with narrative",
            "templates": [
                "{timeframe} ago, I {past_situation}. Everything changed when {turning_point}.",
                "I'll never forget the day {memorable_moment}",
                "There was a time when I {past_struggle}. Then {transformation}.",
                "The moment I realized {insight} changed everything"
            ]
        },
        "controversy": {
            "name": "Controversy",
            "description": "Challenge common beliefs",
            "templates": [
                "Unpopular opinion: {controversial_take}",
                "Hot take: {bold_claim}",
                "Let's be honest: {uncomfortable_truth}",
                "I'm going to say what everyone's thinking: {truth_bomb}"
            ]
        },
        "novelty": {
            "name": "Novelty",
            "description": "Present something new",
            "templates": [
                "I just discovered {new_insight} about {topic}",
                "Here's a fresh take on {topic}",
                "What if we approached {topic} completely differently?",
                "I tried something new with {topic}. The results were {outcome}."
            ]
        },
        "insight": {
            "name": "Insight",
            "description": "Share valuable knowledge",
            "templates": [
                "The difference between {success} and {failure} comes down to {key_insight}",
                "Here's what separates {achievers} from everyone else",
                "The secret to {desired_result} is {insight}",
                "Most people miss this about {topic}: {revelation}"
            ]
        },
        "five_senses": {
            "name": "5 Senses",
            "description": "Create vivid imagery",
            "templates": [
                "You know that feeling when {sensory_experience}?",
                "Picture this: {vivid_scenario}",
                "Remember the last time you {sensory_memory}?",
                "Imagine {sensory_future_pace}"
            ]
        },
        "common_enemies": {
            "name": "Common Enemies",
            "description": "Unite against a shared obstacle",
            "templates": [
                "Can we talk about how {common_enemy} is holding us back?",
                "{obstacle} is the real problem. Here's why.",
                "We've been fighting the wrong battle. {real_enemy} is what we should address.",
                "Everyone's focused on {distraction}. Meanwhile, {actual_problem} is the issue."
            ]
        }
    }

    @classmethod
    def get_hook_point(cls, technique: str, topic: str, context: Dict = None) -> str:
        """Get a hook using a specific technique"""
        hook_point = cls.TECHNIQUES.get(technique, cls.TECHNIQUES['future_pacing'])
        template = random.choice(hook_point['templates'])

        # Default context
        default_context = {
            'positive_outcome': f"feeling confident about {topic}",
            'ideal_scenario': f"mastering {topic}",
            'timeframe': random.choice(['6 months', 'a year', '90 days']),
            'achievement': f"conquered {topic}",
            'desired_state': f"{topic} is no longer a struggle",
            'problem': topic,
            'desired_result': f"master {topic}",
            'frustration': f"struggling with {topic}",
            'action': "change your approach",
            'relatable_feeling': f"overwhelmed by {topic}",
            'relatable_situation': f"you're stuck with {topic}",
            'common_experience': f"facing challenges with {topic}",
            'relatable_struggle': f"you've struggled with {topic}",
            'topic': topic,
            'experience': "in my career",
            'lesson': f"what really works",
            'credential': "years of experience",
            'past_situation': f"struggled with {topic}",
            'turning_point': "I learned this",
            'memorable_moment': "everything clicked",
            'past_struggle': f"couldn't handle {topic}",
            'transformation': "I found a better way",
            'insight': f"the key to {topic}",
            'controversial_take': f"{topic} is misunderstood",
            'bold_claim': f"most advice about {topic} is wrong",
            'uncomfortable_truth': f"{topic} requires more than we think",
            'truth_bomb': f"{topic} isn't the real issue",
            'new_insight': "something surprising",
            'outcome': "unexpected",
            'success': "those who succeed",
            'failure': "those who struggle",
            'key_insight': "one simple shift",
            'achievers': "high performers",
            'revelation': f"it's simpler than you think",
            'sensory_experience': "everything finally makes sense",
            'vivid_scenario': f"confidently handling {topic}",
            'sensory_memory': f"struggled with {topic}",
            'sensory_future_pace': f"easily managing {topic}",
            'common_enemy': f"outdated advice about {topic}",
            'obstacle': "the wrong approach",
            'real_enemy': f"misunderstanding {topic}",
            'distraction': "surface symptoms",
            'actual_problem': "the root cause"
        }

        if context:
            default_context.update(context)

        try:
            return template.format(**default_context)
        except KeyError:
            return f"Let's talk about {topic}"


class VideoShotLibrary:
    """Library of video types and shot types for visual variety"""

    VIDEO_TYPES = {
        "b_roll_storyteller": {
            "name": "B-Roll Storyteller",
            "description": "Overlay visuals of you working, writing, coaching, traveling, or with your planner while your voice narrates.",
            "best_for": "Tips, motivation, or storytelling posts",
            "suggested_shots": ["Close-Up", "Detail/Macro", "POV", "Tracking/Movement"]
        },
        "micro_documentary": {
            "name": "Micro-Documentary",
            "description": "Mix interviews (of you or others), B-roll, and ambient sound.",
            "best_for": "Behind the brand or 'what I've learned as a coach' pieces",
            "suggested_shots": ["Medium Shot", "Close-Up", "Cutaway/Insert", "Wide Shot"]
        },
        "day_in_life": {
            "name": "Day-in-the-Life / Workflow",
            "description": "Real moments—morning routine, content setup, client calls, journaling.",
            "best_for": "Authenticity and relatability",
            "suggested_shots": ["Wide Shot", "POV", "Detail/Macro", "Tracking/Movement"]
        },
        "tutorial_demo": {
            "name": "Tutorial / Demo",
            "description": "Show your planner in action, a journaling method, or productivity technique.",
            "best_for": "Educational content, how-to guides",
            "suggested_shots": ["Over-the-Shoulder", "Close-Up", "Detail/Macro", "Medium Shot"]
        },
        "voiceover_reel": {
            "name": "Voiceover Reel",
            "description": "No talking head at all — just clips + music + your narration.",
            "best_for": "Motivational or emotional posts",
            "suggested_shots": ["Cinematic", "Detail/Macro", "Wide Shot", "Tracking/Movement"]
        },
        "reaction_duet": {
            "name": "Reaction / Duet",
            "description": "React to a trending clip, quote, or topic.",
            "best_for": "Quick engagement boost; lets you show personality",
            "suggested_shots": ["Medium Shot", "Close-Up", "Split Screen"]
        },
        "text_motion": {
            "name": "Text-Only with Motion",
            "description": "On-screen text with music, ambient video, or minimalist motion graphics.",
            "best_for": "Clean way to drop quotes or '1-minute takeaways'",
            "suggested_shots": ["Wide Shot", "Detail/Macro", "Cinematic"]
        },
        "cinematic_sequence": {
            "name": "Cinematic Sequence",
            "description": "Use slow motion, lens flares, or natural light transitions to set a mood.",
            "best_for": "Branding intros, promo reels, or seasonal posts",
            "suggested_shots": ["Wide Shot", "Close-Up", "Low Angle", "Tracking/Movement"]
        }
    }

    SHOT_TYPES = {
        "wide_shot": {
            "name": "Wide Shot (Establishing)",
            "description": "Sets the scene — office, coffee shop, street.",
            "best_for": "Opening context or transitions",
            "examples": ["Office overview", "Coffee shop exterior", "Street scene"]
        },
        "medium_shot": {
            "name": "Medium Shot",
            "description": "Waist-up, your go-to for natural conversation or gestures.",
            "best_for": "Natural conversation, presenting tips",
            "examples": ["Talking to camera", "Gesturing while explaining"]
        },
        "close_up": {
            "name": "Close-Up",
            "description": "Focus on expressions or objects — writing in planner, flipping a page, sipping coffee.",
            "best_for": "Intimacy and detail",
            "examples": ["Facial expressions", "Hand writing", "Coffee cup"]
        },
        "over_shoulder": {
            "name": "Over-the-Shoulder (OTS)",
            "description": "Great for tutorials, journaling, or showing a client call setup.",
            "best_for": "Tutorials, showing work in progress",
            "examples": ["Writing in planner", "Typing on laptop", "Reading notes"]
        },
        "pov": {
            "name": "POV (Point-of-View)",
            "description": "Your hands typing, holding your phone, walking.",
            "best_for": "Immersive and personal moments",
            "examples": ["Walking forward", "Hands typing", "Opening a door"]
        },
        "cutaway": {
            "name": "Cutaway / Insert Shot",
            "description": "B-roll that matches your script — e.g., 'I had to pause and reset' → show you exhaling or closing a notebook.",
            "best_for": "Emphasizing key moments in narration",
            "examples": ["Closing notebook", "Deep breath", "Looking away"]
        },
        "tracking": {
            "name": "Tracking / Movement Shot",
            "description": "You walking through a hallway or into a room.",
            "best_for": "Adding life, direction, and momentum",
            "examples": ["Walking through office", "Entering room", "Moving through space"]
        },
        "angle_shot": {
            "name": "Low Angle / High Angle",
            "description": "Low = power and confidence. High = vulnerability or reflection.",
            "best_for": "Setting tone and emotion",
            "examples": ["Low: looking powerful", "High: looking vulnerable"]
        },
        "detail_macro": {
            "name": "Detail / Macro",
            "description": "Pen tip, hand on planner, morning coffee pour.",
            "best_for": "Texture and rhythm in editing",
            "examples": ["Pen writing", "Coffee pouring", "Page turning"]
        }
    }

    @classmethod
    def get_all_video_types(cls) -> Dict:
        """Get all video types"""
        return cls.VIDEO_TYPES

    @classmethod
    def get_all_shot_types(cls) -> Dict:
        """Get all shot types"""
        return cls.SHOT_TYPES

    @classmethod
    def get_video_type(cls, video_type: str) -> Dict:
        """Get a specific video type"""
        return cls.VIDEO_TYPES.get(video_type, {})

    @classmethod
    def get_shot_type(cls, shot_type: str) -> Dict:
        """Get a specific shot type"""
        return cls.SHOT_TYPES.get(shot_type, {})

    @classmethod
    def suggest_shots_for_video(cls, video_type: str) -> List[str]:
        """Suggest shot types for a specific video type"""
        video = cls.VIDEO_TYPES.get(video_type, {})
        return video.get("suggested_shots", [])


class ContentGenerator:
    """Main content generator class with creative variety"""

    def __init__(self):
        self.style = StyleGuide()
        self.topics = self.load_topics()
        self.hook_library = HookLibrary()
        self.frameworks = MessagingFrameworks()
        self.hook_points = HookPoints()
        self.video_shot_library = VideoShotLibrary()
        self.user_examples = self.load_user_examples()

    def load_user_examples(self) -> Dict:
        """Load user's own content examples - PRIORITIZED over built-in content"""
        import os
        user_file = os.path.join(os.path.dirname(__file__), 'user_examples.json')

        try:
            if os.path.exists(user_file):
                with open(user_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Note: Could not load user examples: {e}")

        # Return empty structure if file doesn't exist or has errors
        return {
            "tips": {},
            "hooks": {},
            "full_scripts": []
        }

    def save_user_example(self, example_type: str, topic: str, content: Dict) -> bool:
        """Save a new user example to the JSON file"""
        import os
        user_file = os.path.join(os.path.dirname(__file__), 'user_examples.json')

        try:
            # Add to current examples
            if example_type == "tip":
                if topic not in self.user_examples["tips"]:
                    self.user_examples["tips"][topic] = []
                self.user_examples["tips"][topic].append(content)
            elif example_type == "hook":
                if topic not in self.user_examples["hooks"]:
                    self.user_examples["hooks"][topic] = []
                self.user_examples["hooks"][topic].append(content)
            elif example_type == "full_script":
                self.user_examples["full_scripts"].append(content)

            # Save to file
            with open(user_file, 'w', encoding='utf-8') as f:
                json.dump(self.user_examples, f, indent=2, ensure_ascii=False)

            return True
        except Exception as e:
            print(f"Error saving user example: {e}")
            return False

    def load_topics(self) -> Dict:
        """Load content topics and themes"""
        return {
            "personal_growth": [
                "dealing with negative people",
                "building confidence",
                "overcoming self-doubt",
                "setting boundaries",
                "managing stress",
                "finding work-life balance",
                "developing resilience",
                "embracing change",
                "overcoming fear",
                "building self-awareness",
                "handling criticism",
                "developing patience",
                "managing expectations",
                "building trust",
                "overcoming perfectionism"
            ],
            "professional_development": [
                "leadership skills",
                "effective communication",
                "time management",
                "networking strategies",
                "career advancement",
                "workplace relationships",
                "project management tips",
                "public speaking",
                "conflict resolution",
                "delegation skills",
                "strategic thinking",
                "decision making",
                "managing teams",
                "giving feedback",
                "handling difficult conversations"
            ],
            "mindset": [
                "positive thinking",
                "growth mindset",
                "self-awareness",
                "emotional intelligence",
                "gratitude practice",
                "mental clarity",
                "self-discipline",
                "motivation strategies",
                "focus and concentration",
                "overcoming limiting beliefs",
                "developing grit",
                "cultivating optimism",
                "managing expectations",
                "building resilience",
                "finding purpose"
            ]
        }

    def generate_instagram_reel(self, topic: str = None, num_tips: int = 3) -> Dict:
        """Generate Instagram Reel content with creative variety"""
        if not topic:
            category = random.choice(list(self.topics.keys()))
            topic = random.choice(self.topics[category])

        # Generate hook using varied techniques
        hook = self._generate_creative_hook(topic)

        # Generate tips with variety
        tips = self.generate_tips(topic, num_tips)

        # Vary the transition
        transitions = [
            f"[start B-roll] Whether in your personal life or professional journey [end B-roll] here are {num_tips} ways to {self.topic_to_action(topic)}.",
            f"[start B-roll] Let me share {num_tips} strategies that actually work [end B-roll] for {topic}.",
            f"Here are {num_tips} things that made all the difference for me with {topic}.",
            f"[start B-roll] I've narrowed it down to {num_tips} key approaches [end B-roll] that really move the needle on {topic}.",
            f"After years of working on this, here are the {num_tips} most important things about {topic}."
        ]

        # Build the reel structure
        reel = {
            "content_type": "Instagram Reel",
            "topic": topic,
            "duration": "55-60 seconds",
            "structure": {
                "hook": {
                    "timestamp": "0-3 seconds",
                    "visual": "Talking Head",
                    "script": hook
                },
                "intro": {
                    "timestamp": "3-8 seconds",
                    "visual": "Talking Head",
                    "script": self.style.get_intro()
                },
                "transition": {
                    "timestamp": "8-12 seconds",
                    "visual": random.choice(["Talking Head → B-roll", "Talking Head with B-roll overlay"]),
                    "script": random.choice(transitions)
                },
                "tips": tips,
                "cta": {
                    "timestamp": "55-60 seconds",
                    "visual": "Talking Head",
                    "script": self.style.get_cta()  # Use varied CTAs
                }
            }
        }

        # Generate full script
        reel["full_script"] = self.compile_reel_script(reel)

        return reel

    def _generate_creative_hook(self, topic: str) -> str:
        """Generate a hook using varied techniques"""

        # PRIORITY 1: Check user's own hooks first (30% chance if available)
        user_hooks = self.user_examples.get("hooks", {}).get(topic, [])
        if user_hooks and random.random() < 0.3:
            # Use user's proven hooks
            return random.choice(user_hooks)["hook"]

        # PRIORITY 2: Use generation methods
        # Randomly choose between different hook generation methods
        method = random.choice(['hook_library', 'hook_point', 'custom'])

        if method == 'hook_library':
            return self.hook_library.get_hook(topic)
        elif method == 'hook_point':
            technique = random.choice(list(self.hook_points.TECHNIQUES.keys()))
            return self.hook_points.get_hook_point(technique, topic)
        else:
            # Custom hooks
            return self._generate_custom_hook(topic)

    def _generate_custom_hook(self, topic: str) -> str:
        """Generate custom hooks with variety"""
        custom_hooks = [
            f"Let's talk about {topic}. Most people get this completely wrong.",
            f"Here's the thing about {topic} nobody wants to admit.",
            f"If you're struggling with {topic}, this might be why.",
            f"I've been thinking a lot about {topic} lately. Here's what I've realized.",
            f"The truth about {topic}? It's simpler than you think.",
            f"Real talk: {topic} doesn't have to be this hard.",
            f"Three years of working on {topic} taught me this.",
            f"Everyone's talking about {topic}. But are they getting it right?",
            f"Here's what changed my perspective on {topic}.",
            f"The biggest misconception about {topic}? Let me break it down."
        ]
        return random.choice(custom_hooks)

    def topic_to_action(self, topic: str) -> str:
        """Convert topic to actionable phrase with variations"""
        action_variations = {
            "dealing with negative people": [
                "work with people you don't get along with",
                "handle difficult personalities",
                "maintain your energy around negativity",
                "set boundaries with toxic people"
            ],
            "building confidence": [
                "boost your confidence",
                "develop unshakeable self-belief",
                "build authentic confidence",
                "trust yourself more"
            ],
            "overcoming self-doubt": [
                "overcome self-doubt",
                "silence your inner critic",
                "move past uncertainty",
                "trust your abilities"
            ],
            "setting boundaries": [
                "set healthy boundaries",
                "protect your energy",
                "say no without guilt",
                "establish clear limits"
            ]
        }

        # Check if we have specific variations for this topic
        if topic in action_variations:
            return random.choice(action_variations[topic])
        # Default variations
        default_actions = [
            f"improve your {topic}",
            f"master {topic}",
            f"approach {topic} differently",
            f"handle {topic} with confidence",
            f"transform your {topic}"
        ]
        return random.choice(default_actions)

    def generate_hooks(self, topic: str, count: int = 3) -> List[str]:
        """Generate varied attention-grabbing hooks"""
        hooks = []
        for _ in range(count):
            hooks.append(self._generate_creative_hook(topic))
        return hooks

    def generate_tips(self, topic: str, count: int = 3) -> List[Dict]:
        """Generate actionable tips with REAL insights from expertise"""

        # PRIORITY 1: Check user's own examples first
        user_tips = self.user_examples.get("tips", {}).get(topic, [])
        if user_tips and len(user_tips) >= count:
            # Use user's tips - they know their voice best
            selected_tips = random.sample(user_tips, count)
            return self._format_tips(selected_tips, count)

        # PRIORITY 2: Built-in tip bank with REAL insights
        tip_bank = {
            "dealing with negative people": [
                {
                    "title": "limit your interaction",
                    "explanation": "Do what you have to do and get the job done, but you don't necessarily need to give them access to your energy.",
                    "b_roll": False
                },
                {
                    "title": "try empathizing",
                    "explanation": "[start B-roll] You don't have to like someone, but if you try to understand where they're coming from [end B-roll] you'd be surprised how a couple of genuine questions can transform a relationship.",
                    "b_roll": True
                },
                {
                    "title": "set clear boundaries",
                    "explanation": "[start B-roll] Let them know what's acceptable and what's not, [end B-roll] then respect your own boundaries. If they want to live in negativity, that's their choice, but you don't have to join them.",
                    "b_roll": True
                },
                {
                    "title": "don't take it personally",
                    "explanation": "Their negativity is about them, not you. [start B-roll] When you realize their behavior reflects their internal state, [end B-roll] it becomes easier to not absorb their energy.",
                    "b_roll": True
                },
                {
                    "title": "focus on solutions, not complaints",
                    "explanation": "When they start complaining, redirect to problem-solving. [start B-roll] Ask 'what would help?' instead of engaging with the negativity. [end B-roll] It shifts the energy of the conversation.",
                    "b_roll": True
                },
                {
                    "title": "protect your peace",
                    "explanation": "You can be professional, you can be kind, but [start B-roll] you don't owe anyone access to your peace of mind. [end B-roll] Guard it like the precious resource it is.",
                    "b_roll": True
                }
            ],
            "building confidence": [
                {
                    "title": "confidence comes from doing, not feeling",
                    "explanation": "[start B-roll] You're not going to feel ready. Do it anyway. [end B-roll] Confidence is built through evidence, and evidence comes from action.",
                    "b_roll": True
                },
                {
                    "title": "track your wins, especially the small ones",
                    "explanation": "Your brain forgets progress. [start B-roll] Write down what you accomplished, even the tiny stuff. [end B-roll] When doubt shows up, you've got receipts.",
                    "b_roll": True
                },
                {
                    "title": "stop waiting for external validation",
                    "explanation": "[start B-roll] If you need everyone's approval, you'll never move. [end B-roll] Build internal confidence - know your worth independent of other people's opinions.",
                    "b_roll": True
                },
                {
                    "title": "competence builds confidence, not the other way around",
                    "explanation": "Get good at something. [start B-roll] Real confidence comes from knowing you can deliver, not from affirmations. [end B-roll] Put in the reps.",
                    "b_roll": True
                },
                {
                    "title": "comparison will kill your confidence",
                    "explanation": "[start B-roll] You're comparing your behind-the-scenes to everyone else's highlight reel. [end B-roll] Stay in your lane. Focus on your own growth.",
                    "b_roll": True
                },
            ],
            "overcoming self-doubt": [
                {
                    "title": "question the doubt",
                    "explanation": "[start B-roll] Don't accept every thought as truth. [end B-roll] Ask yourself: is this doubt based on facts or fear?",
                    "b_roll": True
                },
                {
                    "title": "collect evidence of your capability",
                    "explanation": "Keep a record of times you succeeded despite doubts. [start B-roll] When doubt shows up, review your track record. [end B-roll] Past success predicts future capability.",
                    "b_roll": True
                },
                {
                    "title": "separate feeling from fact",
                    "explanation": "[start B-roll] Just because you feel incapable doesn't mean you are. [end B-roll] Feelings are temporary visitors, not permanent truth.",
                    "b_roll": True
                },
                {
                    "title": "expect doubt and move anyway",
                    "explanation": "Doubt isn't a stop sign, it's scenery on the journey. [start B-roll] Successful people feel doubt too - they just don't let it make decisions. [end B-roll]",
                    "b_roll": True
                },
                {
                    "title": "focus on process, not perfection",
                    "explanation": "[start B-roll] Self-doubt thrives on perfectionism. [end B-roll] Shift your focus to progress and learning. That's where real growth happens.",
                    "b_roll": True
                }
            ],
            "setting boundaries": [
                {
                    "title": "start with small boundaries",
                    "explanation": "[start B-roll] You don't have to overhaul everything at once. [end B-roll] Practice saying no in low-stakes situations first. Build the muscle.",
                    "b_roll": True
                },
                {
                    "title": "communicate clearly, not harshly",
                    "explanation": "Boundaries aren't about being mean, they're about being clear. [start B-roll] You can be kind and firm at the same time. [end B-roll]",
                    "b_roll": True
                },
                {
                    "title": "expect pushback",
                    "explanation": "[start B-roll] When you start setting boundaries, people who benefited from you having none will resist. [end B-roll] That's not a sign you're wrong, it's confirmation you're doing it right.",
                    "b_roll": True
                },
                {
                    "title": "release guilt",
                    "explanation": "Protecting your energy isn't selfish, it's self-respect. [start B-roll] You can't pour from an empty cup. [end B-roll] Your well-being matters.",
                    "b_roll": True
                },
                {
                    "title": "be consistent",
                    "explanation": "[start B-roll] Boundaries only work if you maintain them. [end B-roll] Inconsistency teaches people your limits are negotiable. They're not.",
                    "b_roll": True
                }
            ],
            "leadership skills": [
                {
                    "title": "make the call, then explain",
                    "explanation": "In high-stakes environments, indecision costs more than a wrong decision. [start B-roll] Make the call with the info you have, then bring people along. [end B-roll] You can course-correct, but you can't lead from confusion.",
                    "b_roll": True
                },
                {
                    "title": "your energy sets the tone",
                    "explanation": "[start B-roll] If you're frantic, your team's frantic. If you're steady, they're steady. [end B-roll] You can't fake this - manage your state before you manage your team.",
                    "b_roll": True
                },
                {
                    "title": "build trust before you need it",
                    "explanation": "When the pressure hits, it's too late to build relationships. [start B-roll] Invest in your people when things are calm [end B-roll] so they trust you when things get rough.",
                    "b_roll": True
                },
                {
                    "title": "say the hard thing early",
                    "explanation": "[start B-roll] Address the issue when it's small, not when it's a crisis. [end B-roll] Real leaders don't avoid difficult conversations - they have them before they have to.",
                    "b_roll": True
                },
                {
                    "title": "develop your replacement",
                    "explanation": "Your job isn't to be irreplaceable. [start B-roll] It's to build someone who can do your job so you can do the next one. [end B-roll] That's how you actually move up.",
                    "b_roll": True
                },
            ],
            "delegation skills": [
                {
                    "title": "match the task to the person's growth edge",
                    "explanation": "Don't just delegate what you hate. [start B-roll] Match tasks to where someone's ready to stretch, not where they'll drown or coast. [end B-roll] That's how you build trust and capability at the same time.",
                    "b_roll": True
                },
                {
                    "title": "adjust your delivery to their personality",
                    "explanation": "[start B-roll] Some people need context and the why. Others just want the what and when. [end B-roll] How you deliver the ask matters as much as what you're asking for.",
                    "b_roll": True
                },
                {
                    "title": "be clear about authority and expectations",
                    "explanation": "Tell them exactly what decisions they can make without you. [start B-roll] Vague delegation creates confusion and kills momentum. [end B-roll] Clarity upfront saves everyone time later.",
                    "b_roll": True
                },
                {
                    "title": "follow up without micromanaging",
                    "explanation": "[start B-roll] Check in at agreed milestones, not every five minutes. [end B-roll] You're building capability, not babysitting. Trust the process you set up.",
                    "b_roll": True
                },
                {
                    "title": "own the outcome, share the credit",
                    "explanation": "When it goes well, shine the light on them. When it doesn't, that's on you as the leader. [start B-roll] That's how you build a team that runs through walls for you. [end B-roll]",
                    "b_roll": True
                },
            ],
            "time management": [
                {
                    "title": "protect your high-value hours",
                    "explanation": "[start B-roll] Figure out when you do your best thinking. [end B-roll] Guard those hours for your most important work. Don't waste them on meetings that could be emails.",
                    "b_roll": True
                },
                {
                    "title": "time block, don't just to-do list",
                    "explanation": "A to-do list tells you what. A time block tells you when. [start B-roll] If it's not on your calendar, it's not real. [end B-roll]",
                    "b_roll": True
                },
                {
                    "title": "batch similar tasks together",
                    "explanation": "[start B-roll] Context switching kills productivity. [end B-roll] Group similar tasks - all your calls, all your deep work, all your admin. Your brain will thank you.",
                    "b_roll": True
                },
                {
                    "title": "build in buffer time",
                    "explanation": "Back-to-back meetings all day is a setup for failure. [start B-roll] Leave 15 minutes between commitments. [end B-roll] You need space to think and transition.",
                    "b_roll": True
                },
                {
                    "title": "say no to protect your yes",
                    "explanation": "[start B-roll] Every yes to something unimportant is a no to something that matters. [end B-roll] Be ruthless about what gets your time.",
                    "b_roll": True
                },
            ],
            "effective communication": [
                {
                    "title": "lead with the bottom line",
                    "explanation": "Don't bury your point. [start B-roll] Start with what you need, then explain if needed. [end B-roll] Respect people's time - say it straight.",
                    "b_roll": True
                },
                {
                    "title": "match your communication to your audience",
                    "explanation": "[start B-roll] Executives want the headline. Your team wants the context. [end B-roll] Same message, different delivery. Know who you're talking to.",
                    "b_roll": True
                },
                {
                    "title": "listen to understand, not to respond",
                    "explanation": "If you're thinking about your response, you're not listening. [start B-roll] Hear them out fully before you speak. [end B-roll] Real communication is two-way.",
                    "b_roll": True
                },
                {
                    "title": "over-communicate in high-stakes situations",
                    "explanation": "[start B-roll] When the stakes are high, assume nothing is understood. [end B-roll] Repeat key points. Confirm understanding. Clarity saves crises.",
                    "b_roll": True
                },
                {
                    "title": "own your mistakes immediately",
                    "explanation": "If you mess up, say it fast. [start B-roll] Don't wait, don't spin, don't deflect. [end B-roll] Own it, fix it, move on. That's how you keep trust.",
                    "b_roll": True
                },
            ],
            "managing stress": [
                {
                    "title": "identify what you actually control",
                    "explanation": "[start B-roll] Stress comes from trying to control what you can't. [end B-roll] Make a list - what can you influence, what can't you? Focus your energy accordingly.",
                    "b_roll": True
                },
                {
                    "title": "build buffers before you need them",
                    "explanation": "In high-pressure jobs, you need margin built in. [start B-roll] Time buffers, energy buffers, financial buffers. [end B-roll] Stress hits hardest when you're running on empty.",
                    "b_roll": True
                },
                {
                    "title": "stress is information, not the enemy",
                    "explanation": "[start B-roll] Your stress is telling you something. [end B-roll] Listen to it. What's actually overwhelming you? Don't just push through - address the root.",
                    "b_roll": True
                },
                {
                    "title": "protect your recovery time",
                    "explanation": "You can sprint, but not forever. [start B-roll] Recovery isn't optional, it's strategic. [end B-roll] Guard your off time like it's part of the job - because it is.",
                    "b_roll": True
                },
                {
                    "title": "get real about what 'urgent' actually means",
                    "explanation": "[start B-roll] Not everything that feels urgent is urgent. [end B-roll] Learn to tell the difference. Real urgency is rare - manufactured urgency is everywhere.",
                    "b_roll": True
                },
            ],
        }

        # PRIORITY 3: Mix user tips with built-in tips if needed
        all_available_tips = []

        # Add user tips first (if any)
        if user_tips:
            all_available_tips.extend(user_tips)

        # Add built-in tips
        if topic in tip_bank:
            all_available_tips.extend(tip_bank[topic])
        else:
            # Generate generic tips if no specific ones exist
            all_available_tips.extend(self.generate_creative_generic_tips(topic, count))

        # Select random mix
        selected_tips = random.sample(all_available_tips, min(count, len(all_available_tips)))

        return self._format_tips(selected_tips, count)

    def _format_tips(self, tips: List[Dict], count: int) -> List[Dict]:
        """Format tips with timestamps and visuals"""
        formatted_tips = []
        base_timestamp = 12

        for i, tip in enumerate(tips[:count]):
            timestamp_start = base_timestamp + (i * 13)
            timestamp_end = timestamp_start + 13
            visual = "Talking Head with B-roll overlay" if tip.get("b_roll", False) else "Talking Head"

            formatted_tips.append({
                "number": i + 1,
                "timestamp": f"{timestamp_start}-{timestamp_end} seconds",
                "visual": visual,
                "title": tip["title"],
                "script": f"{i + 1}, {tip['title']}. {tip['explanation']}"
            })

        return formatted_tips

    def generate_creative_generic_tips(self, topic: str, count: int) -> List[Dict]:
        """Generate tips when we don't have topic-specific ones - still avoid platitudes"""
        clean_topic = topic.replace('_', ' ')
        tip_patterns = [
            {
                "title": f"start small, get specific",
                "explanation": f"Don't try to fix everything at once with {clean_topic}. [start B-roll] Pick one thing, get good at it, then move to the next. [end B-roll] Specific beats vague every time.",
                "b_roll": True
            },
            {
                "title": f"find someone who's done it",
                "explanation": f"[start B-roll] You don't have to figure out {clean_topic} from scratch. [end B-roll] Find people ahead of you and learn from what worked for them.",
                "b_roll": True
            },
            {
                "title": f"track what's actually working",
                "explanation": f"You can't improve {clean_topic} if you're guessing. [start B-roll] Measure something - anything. [end B-roll] Data beats feelings when you're trying to get better.",
                "b_roll": True
            },
            {
                "title": f"get honest feedback",
                "explanation": f"[start B-roll] Ask people who'll tell you the truth about your {clean_topic}. [end B-roll] Not people who'll make you feel good - people who'll make you better.",
                "b_roll": True
            },
            {
                "title": f"focus on what you control",
                "explanation": f"A lot of {clean_topic} comes down to what's in your control vs what isn't. [start B-roll] Put your energy where you can actually make a difference. [end B-roll]",
                "b_roll": True
            },
            {
                "title": f"build systems, not just goals",
                "explanation": f"[start B-roll] Goals tell you where you want to go. Systems get you there. [end B-roll] What's the repeatable process for improving your {clean_topic}?",
                "b_roll": True
            },
            {
                "title": f"expect it to be messy at first",
                "explanation": f"Getting better at {clean_topic} isn't a straight line. [start B-roll] You're going to have setbacks. That's not failure, that's the process. [end B-roll]",
                "b_roll": True
            },
            {
                "title": f"protect your energy for what matters",
                "explanation": f"[start B-roll] Not everything deserves your attention. [end B-roll] Be ruthless about where you invest your time and energy with {clean_topic}.",
                "b_roll": True
            },
        ]

        # Randomly select tips
        return random.sample(tip_patterns, min(count, len(tip_patterns)))

    def compile_reel_script(self, reel: Dict) -> str:
        """Compile the full script in order"""
        script_parts = [
            reel["structure"]["hook"]["script"],
            reel["structure"]["intro"]["script"],
            reel["structure"]["transition"]["script"]
        ]

        for tip in reel["structure"]["tips"]:
            script_parts.append(tip["script"])

        script_parts.append(reel["structure"]["cta"]["script"])

        return " ".join(script_parts)

    def generate_content_hooks(self, category: str = None, count: int = 5) -> List[Dict]:
        """Generate hook ideas with massive variety"""
        if not category:
            category = random.choice(list(self.topics.keys()))

        hooks = []
        topics = self.topics.get(category, self.topics["personal_growth"])

        for i in range(count):
            topic = random.choice(topics)
            # Use creative hook generation
            hook = self._generate_creative_hook(topic)
            hooks.append({
                "number": i + 1,
                "category": category,
                "topic": topic,
                "hook": hook,
                "use_case": random.choice([
                    "Instagram Reel, TikTok, YouTube Short",
                    "Instagram Story, Facebook Story",
                    "LinkedIn Post, Tweet Thread",
                    "YouTube Intro, Podcast Opening",
                    "Blog Post Opening, Email Newsletter"
                ])
            })

        return hooks

    def generate_content_framework(self, framework_type: str = None) -> Dict:
        """Generate content using messaging frameworks with variety"""
        if not framework_type:
            # Randomly select a framework
            return self.frameworks.get_random_framework()

        # Try to get specific framework, fall back to random
        framework = self.frameworks.get_framework(framework_type)
        if not framework:
            framework = self.frameworks.get_random_framework()

        return framework

    def generate_custom_content(self, user_topic: str, content_type: str = "reel", num_tips: int = 3) -> Dict:
        """Generate content based on user's custom topic/idea with creativity"""
        # Clean up the topic
        topic = user_topic.strip().lower()

        if content_type == "reel":
            # Generate a reel with the custom topic
            reel = self.generate_instagram_reel(topic, num_tips)
            reel["custom_topic"] = True
            reel["original_input"] = user_topic
            return reel
        elif content_type == "hooks":
            # Generate hooks for the custom topic
            hooks = self.generate_hooks(topic, num_tips)
            return {
                "custom_topic": True,
                "original_input": user_topic,
                "topic": topic,
                "hooks": hooks,
                "use_case": random.choice([
                    "Instagram Reel, TikTok, YouTube Short",
                    "LinkedIn Post, Twitter Thread",
                    "Blog Post, Email Newsletter",
                    "YouTube Video, Podcast Episode"
                ])
            }
        elif content_type == "quick_idea":
            # Generate a quick content idea
            hook = self._generate_creative_hook(topic)
            framework = self.generate_content_framework()
            return {
                "custom_topic": True,
                "original_input": user_topic,
                "topic": topic,
                "hook": hook,
                "format": random.choice([
                    "60-second reel or short-form video",
                    "Instagram carousel post (5-7 slides)",
                    "Twitter/LinkedIn thread (8-10 tweets)",
                    "YouTube video (5-8 minutes)",
                    "Blog post (800-1200 words)"
                ]),
                "cta": self.style.signature_cta,
                "suggested_framework": framework["name"]
            }
        else:
            return {"error": "Invalid content type"}

    def add_custom_topics(self, category: str, topics: List[str]) -> bool:
        """Add custom topics to a category"""
        if category not in self.topics:
            self.topics[category] = []

        # Add topics that aren't already in the list
        for topic in topics:
            clean_topic = topic.strip().lower()
            if clean_topic and clean_topic not in self.topics[category]:
                self.topics[category].append(clean_topic)

        return True
