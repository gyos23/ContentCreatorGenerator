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


def print_header(text: str):
    """Print formatted header"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")


def print_reel(reel: Dict):
    """Print Instagram Reel in formatted way"""
    print_header(f"Instagram Reel: {reel['topic'].title()}")

    print("📱 FULL SCRIPT:")
    print("-" * 70)
    print(reel["full_script"])
    print()

    print("\n📋 DETAILED BREAKDOWN:")
    print("-" * 70)
    structure = reel["structure"]

    print(f"\n🎣 HOOK ({structure['hook']['timestamp']})")
    print(f"Visual: {structure['hook']['visual']}")
    print(f"Script: {structure['hook']['script']}")

    print(f"\n👋 INTRO ({structure['intro']['timestamp']})")
    print(f"Visual: {structure['intro']['visual']}")
    print(f"Script: {structure['intro']['script']}")

    print(f"\n🔄 TRANSITION ({structure['transition']['timestamp']})")
    print(f"Visual: {structure['transition']['visual']}")
    print(f"Script: {structure['transition']['script']}")

    for tip in structure['tips']:
        print(f"\n💡 TIP #{tip['number']} ({tip['timestamp']})")
        print(f"Visual: {tip['visual']}")
        print(f"Title: {tip['title'].upper()}")
        print(f"Script: {tip['script']}")

    print(f"\n📢 CALL TO ACTION ({structure['cta']['timestamp']})")
    print(f"Visual: {structure['cta']['visual']}")
    print(f"Script: {structure['cta']['script']}")

    print("\n" + "=" * 70)


def print_hooks(hooks: List[Dict]):
    """Print hooks in formatted way"""
    print_header("Content Hook Ideas")

    for hook in hooks:
        print(f"\n{hook['number']}. {hook['topic'].upper()}")
        print(f"   Category: {hook['category'].replace('_', ' ').title()}")
        print(f"   Hook: {hook['hook']}")
        print(f"   Use for: {hook['use_case']}")
        print()

    print("=" * 70)


def print_framework(framework: Dict):
    """Print content framework"""
    print_header(framework['name'])

    print("📝 STRUCTURE:")
    for i, step in enumerate(framework['structure'], 1):
        print(f"  {i}. {step}")

    print(f"\n✅ Best for: {framework['best_for']}")
    print("\n" + "=" * 70)


def main():
    """Main application loop"""
    generator = ContentGenerator()

    print("\n" + "🎬" * 35)
    print_header("Social Media Content Generator")
    print("Generate engaging content ideas in your unique style!")
    print("Created for: Dorian - Personal Growth & Development Creator")
    print("🎬" * 35)

    while True:
        print("\n📋 CONTENT OPTIONS:")
        print("  1. Generate Instagram Reel (Problem-Solution Format)")
        print("  2. Generate Content Hooks (5 ideas)")
        print("  3. Generate Content Hook by Category")
        print("  4. View Content Frameworks")
        print("  5. Generate Random Quick Content Ideas")
        print("  6. Exit")

        choice = input("\n👉 Choose an option (1-6): ").strip()

        if choice == "1":
            print("\n📝 REEL TOPICS:")
            categories = list(generator.topics.keys())
            for i, category in enumerate(categories, 1):
                print(f"  {i}. {category.replace('_', ' ').title()}")

            topic_choice = input("\n👉 Choose category (or press Enter for random): ").strip()

            if topic_choice and topic_choice.isdigit() and 1 <= int(topic_choice) <= len(categories):
                category = categories[int(topic_choice) - 1]
                topic = random.choice(generator.topics[category])
            else:
                topic = None

            print("\n⚙️  Generating your Instagram Reel...")
            reel = generator.generate_instagram_reel(topic)
            print_reel(reel)

        elif choice == "2":
            print("\n⚙️  Generating 5 content hooks...")
            hooks = generator.generate_content_hooks(count=5)
            print_hooks(hooks)

        elif choice == "3":
            print("\n📝 CATEGORIES:")
            categories = list(generator.topics.keys())
            for i, category in enumerate(categories, 1):
                print(f"  {i}. {category.replace('_', ' ').title()}")

            cat_choice = input("\n👉 Choose category: ").strip()

            if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
                category = categories[int(cat_choice) - 1]
                count = input("👉 How many hooks? (default 5): ").strip()
                count = int(count) if count.isdigit() else 5

                print(f"\n⚙️  Generating {count} hooks for {category}...")
                hooks = generator.generate_content_hooks(category, count)
                print_hooks(hooks)

        elif choice == "4":
            print("\n📝 FRAMEWORKS:")
            print("  1. Problem-Solution Framework")
            print("  2. Storytelling Framework")
            print("  3. Listicle Framework")

            fw_choice = input("\n👉 Choose framework: ").strip()

            framework_map = {
                "1": "problem-solution",
                "2": "storytelling",
                "3": "listicle"
            }

            framework_type = framework_map.get(fw_choice, "problem-solution")
            framework = generator.generate_content_framework(framework_type)
            print_framework(framework)

        elif choice == "5":
            print("\n⚙️  Generating quick content ideas...")
            print_header("Quick Content Ideas")

            category = random.choice(list(generator.topics.keys()))
            topics = random.sample(generator.topics[category], min(3, len(generator.topics[category])))

            for i, topic in enumerate(topics, 1):
                hooks = generator.generate_hooks(topic, 1)
                print(f"\n{i}. TOPIC: {topic.upper()}")
                print(f"   Hook: {hooks[0]}")
                print(f"   Format: 60-second reel or short-form video")
                print(f"   CTA: {generator.style.signature_cta}")

            print("\n" + "=" * 70)

        elif choice == "6":
            print("\n👋 Thanks for using Content Generator!")
            print("💪 Let's grow together!")
            break

        else:
            print("\n❌ Invalid choice. Please choose 1-6.")


if __name__ == "__main__":
    main()
