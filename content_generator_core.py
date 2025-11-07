#!/usr/bin/env python3
"""
Social Media Content Generator
Generates engaging content ideas in your unique style to grow engagement and business.
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
        """Generate credibility statement"""
        return f"Hi my name is {self.name}. I'm a {self.credentials['day_job']} by day and by night I {self.credentials['mission']}."


class ContentGenerator:
    """Main content generator class"""

    def __init__(self):
        self.style = StyleGuide()
        self.topics = self.load_topics()

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
                "embracing change"
            ],
            "professional_development": [
                "leadership skills",
                "effective communication",
                "time management",
                "networking strategies",
                "career advancement",
                "workplace relationships",
                "project management tips",
                "public speaking"
            ],
            "mindset": [
                "positive thinking",
                "growth mindset",
                "self-awareness",
                "emotional intelligence",
                "gratitude practice",
                "mental clarity",
                "self-discipline",
                "motivation strategies"
            ]
        }

    def generate_instagram_reel(self, topic: str = None, num_tips: int = 3) -> Dict:
        """Generate Instagram Reel content in Dorian's style"""
        if not topic:
            category = random.choice(list(self.topics.keys()))
            topic = random.choice(self.topics[category])

        # Generate hook
        hooks = self.generate_hooks(topic)
        hook = hooks[0]

        # Generate tips
        tips = self.generate_tips(topic, num_tips)

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
                    "visual": "Talking Head → B-roll",
                    "script": f"[start B-roll] Whether in your personal life or professional journey [end B-roll] here are {num_tips} ways to {self.topic_to_action(topic)}."
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

    def topic_to_action(self, topic: str) -> str:
        """Convert topic to actionable phrase"""
        action_map = {
            "dealing with negative people": "work with people you don't get along with",
            "building confidence": "boost your confidence",
            "overcoming self-doubt": "overcome self-doubt",
            "setting boundaries": "set healthy boundaries",
            "managing stress": "manage stress effectively",
            "finding work-life balance": "achieve work-life balance",
            "leadership skills": "become a better leader",
            "effective communication": "communicate more effectively",
            "time management": "manage your time better"
        }
        return action_map.get(topic, f"improve your {topic}")

    def generate_hooks(self, topic: str, count: int = 3) -> List[str]:
        """Generate attention-grabbing hooks"""
        hook_templates = [
            "{problem}. The easiest thing to do is {common_solution}. But the reality is that's not always an option.",
            "{problem}. Everyone tells you to {common_solution}. But what if there's a better way?",
            "{problem}. You've probably tried {common_solution}. Here's why that might not work.",
            "{misconception}. But here's the truth that most people miss.",
            "{problem}. And it's costing you more than you think."
        ]

        # Topic-specific problems and solutions
        problem_solutions = {
            "dealing with negative people": {
                "problem": "Negative people",
                "common_solution": "get rid of negative people when you don't agree with them",
                "misconception": "Most people think avoiding negativity means cutting everyone out"
            },
            "building confidence": {
                "problem": "Low confidence",
                "common_solution": "just fake it till you make it",
                "misconception": "People think confidence comes from never feeling doubt"
            },
            "setting boundaries": {
                "problem": "Saying yes to everything",
                "common_solution": "just say no more often",
                "misconception": "Most people think boundaries mean being selfish"
            }
        }

        # Generate hooks
        hooks = []
        for template in hook_templates[:count]:
            params = problem_solutions.get(topic, {
                "problem": topic.replace("_", " ").title(),
                "common_solution": "ignore it",
                "misconception": f"Most people misunderstand {topic}"
            })
            hooks.append(template.format(**params))

        return hooks

    def generate_tips(self, topic: str, count: int = 3) -> List[Dict]:
        """Generate actionable tips for the topic"""
        # Sample tip bank - in a real app, this would be much larger
        tip_bank = {
            "dealing with negative people": [
                {
                    "title": "limit your interaction",
                    "explanation": "Do what you have to do and get the job done, but you don't necessarily need to give them access to your energy.",
                    "b_roll": False
                },
                {
                    "title": "try empathizing",
                    "explanation": "[start B-roll] You don't have to like someone, but if you try to understand where they're coming [end B-roll] from you'd be surprised with a couple of questions coming from a genuine place how far that can take you in a relationship with someone.",
                    "b_roll": True
                },
                {
                    "title": "set clear boundaries",
                    "explanation": "[start B-roll] You have to let them know what's acceptable, what's not acceptable, [end B-roll] and then you have to personally respect your own boundaries. If they wanna live in negativity, that's cool, but you don't have to live there.",
                    "b_roll": True
                }
            ],
            "building confidence": [
                {
                    "title": "celebrate small wins",
                    "explanation": "Start tracking your daily accomplishments, no matter how small. Confidence builds when you see evidence of your progress.",
                    "b_roll": False
                },
                {
                    "title": "practice self-compassion",
                    "explanation": "[start B-roll] Talk to yourself like you'd talk to a friend. [end B-roll] When you mess up, acknowledge it without the harsh criticism. That's how real confidence grows.",
                    "b_roll": True
                },
                {
                    "title": "take action before you feel ready",
                    "explanation": "[start B-roll] Confidence doesn't come before action, it comes from taking action. [end B-roll] Start small, but start now. Each step forward builds your belief in yourself.",
                    "b_roll": True
                }
            ]
        }

        # Get tips for topic or generate generic ones
        tips = tip_bank.get(topic, self.generate_generic_tips(topic, count))[:count]

        # Format tips with timestamps and visuals
        formatted_tips = []
        base_timestamp = 12
        for i, tip in enumerate(tips):
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

    def generate_generic_tips(self, topic: str, count: int) -> List[Dict]:
        """Generate generic tips for any topic"""
        generic_tips = [
            {
                "title": f"start with awareness",
                "explanation": f"You can't change what you don't acknowledge. Take time to recognize when {topic.replace('_', ' ')} shows up in your life.",
                "b_roll": False
            },
            {
                "title": f"take small consistent actions",
                "explanation": f"[start B-roll] Progress isn't about massive leaps. [end B-roll] It's about showing up every day and doing what you can with what you have.",
                "b_roll": True
            },
            {
                "title": f"learn from setbacks",
                "explanation": f"[start B-roll] Every challenge is feedback, not failure. [end B-roll] Use what doesn't work to inform what will. That's how you grow.",
                "b_roll": True
            }
        ]
        return generic_tips[:count]

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
        """Generate hook ideas for various content"""
        if not category:
            category = random.choice(list(self.topics.keys()))

        hooks = []
        topics = self.topics.get(category, self.topics["personal_growth"])

        for i in range(count):
            topic = random.choice(topics)
            hook_list = self.generate_hooks(topic, 1)
            hooks.append({
                "number": i + 1,
                "category": category,
                "topic": topic,
                "hook": hook_list[0],
                "use_case": "Instagram Reel, TikTok, YouTube Short"
            })

        return hooks

    def generate_content_framework(self, framework_type: str = "problem-solution") -> Dict:
        """Generate content using specific frameworks"""
        frameworks = {
            "problem-solution": {
                "name": "Problem-Solution Framework",
                "structure": [
                    "Hook: Present the problem",
                    "Agitate: Why it matters",
                    "Solution: Your approach",
                    "Proof: Why it works",
                    "Call to Action"
                ],
                "best_for": "Educational content, how-to guides"
            },
            "storytelling": {
                "name": "Storytelling Framework",
                "structure": [
                    "Hook: The moment everything changed",
                    "Setup: Where you were before",
                    "Conflict: What challenged you",
                    "Resolution: How you overcame it",
                    "Lesson: What others can learn",
                    "Call to Action"
                ],
                "best_for": "Personal brand building, connection"
            },
            "listicle": {
                "name": "Listicle Framework",
                "structure": [
                    "Hook: Promise specific number of tips",
                    "Credibility: Why you're qualified",
                    "Tip 1: With explanation",
                    "Tip 2: With explanation",
                    "Tip 3: With explanation",
                    "Summary: Key takeaway",
                    "Call to Action"
                ],
                "best_for": "Quick value, easy consumption"
            }
        }

        return frameworks.get(framework_type, frameworks["problem-solution"])

    def generate_custom_content(self, user_topic: str, content_type: str = "reel", num_tips: int = 3) -> Dict:
        """Generate content based on user's custom topic/idea"""
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
                "use_case": "Instagram Reel, TikTok, YouTube Short"
            }
        elif content_type == "quick_idea":
            # Generate a quick content idea
            hooks = self.generate_hooks(topic, 1)
            return {
                "custom_topic": True,
                "original_input": user_topic,
                "topic": topic,
                "hook": hooks[0],
                "format": "60-second reel or short-form video",
                "cta": self.style.signature_cta,
                "suggested_framework": "Problem-Solution Format"
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
