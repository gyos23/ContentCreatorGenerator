# Usage Examples

## Example 1: Generate an Instagram Reel

```bash
python3 content_generator.py
# Choose option 1
# Choose category 1 (Personal Growth)
# Get a full 60-second reel script with timestamps
```

**Sample Output:**
```
Instagram Reel: Dealing With Negative People

FULL SCRIPT:
Talking head video
Negative people. The easiest thing to do is to get rid of negative people...
[Complete script with timing and B-roll markers]
```

## Example 2: Generate Content Hooks

```bash
python3 content_generator.py
# Choose option 2
# Get 5 hook ideas instantly
```

**Sample Output:**
```
1. DEALING WITH NEGATIVE PEOPLE
   Category: Personal Growth
   Hook: Negative people. The easiest thing to do is to get rid of...
   Use for: Instagram Reel, TikTok, YouTube Short
```

## Example 3: View Content Frameworks

```bash
python3 content_generator.py
# Choose option 4
# Choose framework type (1-3)
# Learn the structure
```

## Example 4: Quick Content Ideas

```bash
python3 content_generator.py
# Choose option 5
# Get 3 instant content ideas
```

## Tips for Best Results

1. **Customize the Output**: The generated content is a starting point. Add your personal experiences and examples.

2. **Mix and Match**: Use different hooks with different frameworks for variety.

3. **Track What Works**: Note which topics and hooks get the most engagement.

4. **Stay Consistent**: Use your signature CTA ("Let's grow together") to build brand recognition.

5. **Add Visuals**: The B-roll markers show exactly where to add supporting footage.

## Customizing Your Style

To customize the generator with your own credentials and style:

1. Open `content_generator.py`
2. Modify the `StyleGuide` class (around line 14):

```python
self.name = "Your Name"
self.credentials = {
    "day_job": "your day job description",
    "mission": "your content mission"
}
self.signature_cta = "Your signature sign-off"
```

## Adding New Topics

To add your own topics:

1. Open `content_generator.py`
2. Find the `load_topics()` method (around line 25)
3. Add your topics to the appropriate category or create a new category:

```python
"your_category": [
    "topic 1",
    "topic 2",
    "topic 3"
]
```

## Adding Custom Tips

To add custom tips for specific topics:

1. Find the `generate_tips()` method (around line 150)
2. Add your topic to the `tip_bank` dictionary:

```python
"your_topic": [
    {
        "title": "tip title",
        "explanation": "detailed explanation...",
        "b_roll": True  # or False
    }
]
```

## Content Categories Currently Available

- **Personal Growth**: 8 topics including confidence, boundaries, stress management
- **Professional Development**: 8 topics including leadership, communication, time management
- **Mindset**: 8 topics including positive thinking, emotional intelligence, self-discipline

Expand these as you discover what resonates with your audience!
