from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sys
import os

# Add parent directory to path to import content_generator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content_generator_core import ContentGenerator

app = Flask(__name__, static_folder='../public', static_url_path='')
CORS(app)

# Initialize generator
generator = ContentGenerator()


@app.route('/')
def home():
    """Serve the main page"""
    # Try multiple paths to find index.html
    possible_paths = [
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'index.html'),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html'),
        '/var/task/index.html',  # Vercel path
        './index.html',
        '../index.html',
    ]

    for index_path in possible_paths:
        try:
            if os.path.exists(index_path):
                with open(index_path, 'r', encoding='utf-8') as f:
                    return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
        except Exception as e:
            continue

    # Fallback to API info page
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Social Media Content Generator</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { font-family: system-ui; max-width: 800px; margin: 40px auto; padding: 20px; }
            h1 { color: #667eea; }
            .error { background: #fff3cd; padding: 15px; border-radius: 8px; margin: 20px 0; }
            ul { line-height: 2; }
        </style>
    </head>
    <body>
        <h1>🎬 Social Media Content Generator API</h1>
        <div class="error">
            <strong>Note:</strong> Web interface could not be loaded. Using API endpoints directly.
        </div>

        <h2>✅ API is Running</h2>
        <p>Available Endpoints:</p>
        <ul>
            <li><strong>GET /api/topics</strong> - Get all available topics</li>
            <li><strong>POST /api/generate/reel</strong> - Generate Instagram Reel</li>
            <li><strong>POST /api/generate/hooks</strong> - Generate content hooks</li>
            <li><strong>POST /api/generate/quick-ideas</strong> - Generate quick ideas</li>
            <li><strong>GET /api/frameworks</strong> - Get content frameworks</li>
            <li><strong>POST /api/generate/custom</strong> - Generate custom content</li>
        </ul>

        <h3>Example API Call:</h3>
        <pre style="background: #f5f5f5; padding: 15px; border-radius: 5px; overflow-x: auto;">
curl -X POST https://your-app.vercel.app/api/generate/reel \\
  -H "Content-Type: application/json" \\
  -d '{"topic": "building confidence", "num_tips": 3}'
        </pre>
    </body>
    </html>
    """, 200, {'Content-Type': 'text/html; charset=utf-8'}


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


@app.route('/api/video-types', methods=['GET'])
def get_video_types():
    """Get all video types for mix-and-match"""
    try:
        from content_generator_core import VideoShotLibrary
        video_types = VideoShotLibrary.get_all_video_types()

        return jsonify({
            'success': True,
            'video_types': video_types
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/shot-types', methods=['GET'])
def get_shot_types():
    """Get all shot types for mix-and-match"""
    try:
        from content_generator_core import VideoShotLibrary
        shot_types = VideoShotLibrary.get_all_shot_types()

        return jsonify({
            'success': True,
            'shot_types': shot_types
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/video-shots/<video_type>', methods=['GET'])
def get_suggested_shots(video_type):
    """Get suggested shot types for a specific video type"""
    try:
        from content_generator_core import VideoShotLibrary
        suggested = VideoShotLibrary.suggest_shots_for_video(video_type)
        video_info = VideoShotLibrary.get_video_type(video_type)

        return jsonify({
            'success': True,
            'video_type': video_info,
            'suggested_shots': suggested
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


# Catch-all route for SPA (must be last)
@app.route('/<path:path>')
def catch_all(path):
    """Catch all routes and serve index.html for SPA routing"""
    # If it's an API call that didn't match, return 404
    if path.startswith('api/'):
        return jsonify({'error': 'Endpoint not found'}), 404

    # Otherwise serve the main HTML page
    return home()


# For Vercel serverless function
# Vercel will use the app directly
app_handler = app


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
