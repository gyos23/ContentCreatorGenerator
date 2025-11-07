from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add parent directory to path to import content_generator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content_generator_core import ContentGenerator

app = Flask(__name__)
CORS(app)

# Initialize generator
generator = ContentGenerator()


@app.route('/')
def home():
    """Serve the main page"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Social Media Content Generator</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h1>Social Media Content Generator API</h1>
        <p>Welcome! The API is running.</p>
        <p>Visit <a href="/app">/app</a> for the content generator interface.</p>

        <h2>Available Endpoints:</h2>
        <ul>
            <li>GET /api/topics - Get all available topics</li>
            <li>POST /api/generate/reel - Generate Instagram Reel</li>
            <li>POST /api/generate/hooks - Generate content hooks</li>
            <li>GET /api/frameworks - Get content frameworks</li>
        </ul>
    </body>
    </html>
    """


@app.route('/api/topics', methods=['GET'])
def get_topics():
    """Get all available topics"""
    return jsonify({
        'success': True,
        'topics': generator.topics
    })


@app.route('/api/generate/reel', methods=['POST'])
def generate_reel():
    """Generate an Instagram Reel"""
    try:
        data = request.get_json() or {}
        topic = data.get('topic')
        num_tips = data.get('num_tips', 3)

        reel = generator.generate_instagram_reel(topic, num_tips)

        return jsonify({
            'success': True,
            'reel': reel
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/generate/hooks', methods=['POST'])
def generate_hooks():
    """Generate content hooks"""
    try:
        data = request.get_json() or {}
        category = data.get('category')
        count = data.get('count', 5)

        hooks = generator.generate_content_hooks(category, count)

        return jsonify({
            'success': True,
            'hooks': hooks
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/generate/quick-ideas', methods=['POST'])
def generate_quick_ideas():
    """Generate quick content ideas"""
    try:
        data = request.get_json() or {}
        count = data.get('count', 3)

        import random
        category = random.choice(list(generator.topics.keys()))
        topics = random.sample(generator.topics[category], min(count, len(generator.topics[category])))

        ideas = []
        for i, topic in enumerate(topics, 1):
            hooks = generator.generate_hooks(topic, 1)
            ideas.append({
                'number': i,
                'topic': topic,
                'hook': hooks[0],
                'format': '60-second reel or short-form video',
                'cta': generator.style.signature_cta
            })

        return jsonify({
            'success': True,
            'ideas': ideas
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/frameworks', methods=['GET'])
def get_frameworks():
    """Get all content frameworks"""
    try:
        frameworks = {
            'problem-solution': generator.generate_content_framework('problem-solution'),
            'storytelling': generator.generate_content_framework('storytelling'),
            'listicle': generator.generate_content_framework('listicle')
        }

        return jsonify({
            'success': True,
            'frameworks': frameworks
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/framework/<framework_type>', methods=['GET'])
def get_framework(framework_type):
    """Get a specific content framework"""
    try:
        framework = generator.generate_content_framework(framework_type)

        return jsonify({
            'success': True,
            'framework': framework
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/generate/custom', methods=['POST'])
def generate_custom():
    """Generate content based on user's custom topic/idea"""
    try:
        data = request.get_json() or {}
        user_topic = data.get('topic', '').strip()
        content_type = data.get('content_type', 'reel')
        num_tips = data.get('num_tips', 3)

        if not user_topic:
            return jsonify({
                'success': False,
                'error': 'Please provide a topic'
            }), 400

        result = generator.generate_custom_content(user_topic, content_type, num_tips)

        return jsonify({
            'success': True,
            'content': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


# For Vercel serverless function
def handler(request):
    """Vercel serverless function handler"""
    with app.app_context():
        return app.full_dispatch_request()


if __name__ == '__main__':
    app.run(debug=True)
