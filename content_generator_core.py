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
        self.tone = "conversational, empowering, actionable"

    def get_intro(self) -> str:
        """Generate credibility statement with variations"""
        intros = [
            f"Hi my name is {self.name}. I'm a {self.credentials['day_job']} by day and by night I {self.credentials['mission']}.",
            f"Hey, I'm {self.name}. By day I work as a {self.credentials['day_job']}, and in my free time I {self.credentials['mission']}.",
            f"I'm {self.name}, a {self.credentials['day_job']} who's passionate about helping others grow. I {self.credentials['mission']}.",
            f"Quick intro - I'm {self.name}. Day job: {self.credentials['day_job']}. But what I really love is helping people grow and develop.",
        ]
        return random.choice(intros)


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


class ContentGenerator:
    """Main content generator class with creative variety"""

    def __init__(self):
        self.style = StyleGuide()
        self.topics = self.load_topics()
        self.hook_library = HookLibrary()
        self.frameworks = MessagingFrameworks()
        self.hook_points = HookPoints()

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
                    "script": self.style.signature_cta
                }
            }
        }

        # Generate full script
        reel["full_script"] = self.compile_reel_script(reel)

        return reel

    def _generate_creative_hook(self, topic: str) -> str:
        """Generate a hook using varied techniques"""
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
        """Generate actionable tips with massive variety"""
        # Expanded tip bank with many more variations
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
                    "title": "celebrate small wins",
                    "explanation": "Start tracking your daily accomplishments, no matter how small. [start B-roll] Confidence builds when you have evidence of your progress. [end B-roll]",
                    "b_roll": True
                },
                {
                    "title": "practice self-compassion",
                    "explanation": "[start B-roll] Talk to yourself like you'd talk to a friend. [end B-roll] When you mess up, acknowledge it without harsh criticism. Real confidence grows from self-acceptance.",
                    "b_roll": True
                },
                {
                    "title": "take action before you feel ready",
                    "explanation": "[start B-roll] Confidence doesn't come before action, it comes from taking action. [end B-roll] Start small, but start now. Each step forward builds your belief in yourself.",
                    "b_roll": True
                },
                {
                    "title": "own your expertise",
                    "explanation": "Stop downplaying what you know. [start B-roll] You've earned your knowledge through experience. [end B-roll] Share it with confidence.",
                    "b_roll": True
                },
                {
                    "title": "reframe failure as feedback",
                    "explanation": "[start B-roll] Every setback is data, not a judgment of your worth. [end B-roll] When you see mistakes as information, confidence becomes unshakeable.",
                    "b_roll": True
                },
                {
                    "title": "surround yourself with believers",
                    "explanation": "The people around you shape your self-perception. [start B-roll] Choose relationships that reflect your potential back to you, [end B-roll] not your limitations.",
                    "b_roll": True
                }
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
                    "title": "lead by example",
                    "explanation": "[start B-roll] Your team watches what you do more than what you say. [end B-roll] Model the behavior and standards you expect from others.",
                    "b_roll": True
                },
                {
                    "title": "develop your people",
                    "explanation": "Great leaders create more leaders, not followers. [start B-roll] Invest in your team's growth. Their success is your success. [end B-roll]",
                    "b_roll": True
                },
                {
                    "title": "make decisions with clarity",
                    "explanation": "[start B-roll] Indecision creates chaos. [end B-roll] Gather input, trust your judgment, and commit to a direction. You can adjust as you go.",
                    "b_roll": True
                },
                {
                    "title": "give credit freely",
                    "explanation": "Secure leaders celebrate their team's wins. [start B-roll] When you shine a light on others, it reflects back on your leadership. [end B-roll]",
                    "b_roll": True
                },
                {
                    "title": "stay humble and curious",
                    "explanation": "[start B-roll] The moment you think you know everything is when you stop growing. [end B-roll] Ask questions. Listen more than you speak.",
                    "b_roll": True
                }
            ]
        }

        # Get topic-specific tips or generate creative generic ones
        if topic in tip_bank:
            available_tips = tip_bank[topic]
            # Randomly select from available tips
            selected_tips = random.sample(available_tips, min(count, len(available_tips)))
        else:
            selected_tips = self.generate_creative_generic_tips(topic, count)

        # Format tips with timestamps and visuals
        formatted_tips = []
        base_timestamp = 12
        for i, tip in enumerate(selected_tips):
            timestamp_start = base_timestamp + (i * 13)
            timestamp_end = timestamp_start + 13
            visual = "Talking Head with B-roll overlay" if tip["b_roll"] else "Talking Head"

            formatted_tips.append({
                "number": i + 1,
                "timestamp": f"{timestamp_start}-{timestamp_end} seconds",
                "visual": visual,
                "title": tip["title"],
                "script": f"{i + 1}, {tip['title']}. {tip['explanation']}"
            })

        return formatted_tips

    def generate_creative_generic_tips(self, topic: str, count: int) -> List[Dict]:
        """Generate creative generic tips with variety"""
        # Much more varied generic tip patterns
        tip_patterns = [
            {
                "title": f"start with self-awareness",
                "explanation": f"[start B-roll] You can't change what you don't acknowledge. [end B-roll] Notice when {topic.replace('_', ' ')} shows up in your life and what triggers it.",
                "b_roll": True
            },
            {
                "title": f"take consistent small actions",
                "explanation": f"Progress isn't about massive leaps. [start B-roll] It's about showing up every day [end B-roll] and doing what you can with what you have.",
                "b_roll": True
            },
            {
                "title": f"learn from every experience",
                "explanation": f"[start B-roll] Every challenge with {topic.replace('_', ' ')} is feedback, not failure. [end B-roll] Use what doesn't work to inform what will.",
                "b_roll": True
            },
            {
                "title": f"find your why",
                "explanation": f"When you know why {topic.replace('_', ' ')} matters to you, [start B-roll] the how becomes easier to figure out. [end B-roll] Motivation follows meaning.",
                "b_roll": True
            },
            {
                "title": f"embrace discomfort",
                "explanation": f"[start B-roll] Growth and comfort don't coexist. [end B-roll] If {topic.replace('_', ' ')} feels challenging, that's a sign you're expanding.",
                "b_roll": True
            },
            {
                "title": f"seek feedback",
                "explanation": f"You can't see your own blind spots. [start B-roll] Ask people you trust how you're doing with {topic.replace('_', ' ')}. [end B-roll] Their perspective is valuable.",
                "b_roll": True
            },
            {
                "title": f"practice patience",
                "explanation": f"[start B-roll] Real change takes time. [end B-roll] Trust the process with {topic.replace('_', ' ')}. Small improvements compound into major transformation.",
                "b_roll": True
            },
            {
                "title": f"celebrate progress",
                "explanation": f"Don't wait for perfection to acknowledge growth. [start B-roll] Notice and celebrate improvements with {topic.replace('_', ' ')}, [end B-roll] no matter how small.",
                "b_roll": True
            },
            {
                "title": f"build support systems",
                "explanation": f"[start B-roll] You don't have to figure out {topic.replace('_', ' ')} alone. [end B-roll] Connect with people who get it and can support your journey.",
                "b_roll": True
            },
            {
                "title": f"reflect regularly",
                "explanation": f"Take time to review what's working and what isn't with {topic.replace('_', ' ')}. [start B-roll] Reflection turns experience into wisdom. [end B-roll]",
                "b_roll": True
            }
        ]

        # Randomly select tips
        return random.sample(tip_patterns, min(count, len(tip_patterns)))

    def compile_reel_script(self, reel: Dict) -> str:
        """Compile the full script in order"""
        script_parts = [
            "Talking head video",
            reel["structure"]["hook"]["script"],
            reel["structure"]["intro"]["script"],
            reel["structure"]["transition"]["script"]
        ]

        for tip in reel["structure"]["tips"]:
            script_parts.append(tip["script"])

        script_parts.append(reel["structure"]["cta"]["script"])
        script_parts.append("[end visual]")

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
