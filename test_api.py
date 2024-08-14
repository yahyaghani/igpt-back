from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat')
def get_chat_data():
    chat_data = [
        {
            "imgSrc": "https://img.freepik.com/premium-vector/online-communication-with-chat-bot-concept-chatbot-robot-providing-online-assistance-chat-gpt_530733-3104.jpg",
            "character": "Emily",
            "markdown": "explain about skrew for 5 years old with table and graph"
        },
        {
            "imgSrc": "https://img.freepik.com/premium-photo/teenager-student-girl-yellow-pointing-finger-side_1368-40175.jpg",
            "character": "AI Assistant",
            "markdown": "## What is a Screw?\n\nA **screw** is a tiny tool that helps hold things together. It looks like a little stick with a spiral around it. We use screws to keep things like toys, furniture, or even your bookshelves from falling apart!\n\n### How Does a Screw Work?\n\n- **Twist the screw**: You turn it with a tool called a **screwdriver**.\n- **Goes into wood or plastic**: The screw spins and digs into the wood or plastic, holding it tight.\n- **Keeps things together**: Once it's in, it stays there and keeps the parts from moving!\n\n### Table: Parts of a Screw\n\n| Part Name  | What It Does                         |\n|------------|--------------------------------------|\n| **Head**   | The flat top that you twist with the screwdriver. |\n| **Thread** | The spiral part that digs into the wood. |\n| **Tip**    | The sharp point that helps the screw start going into the wood. |\n\n### Graph: How a Screw Holds Things Together\n\n```plaintext\n+------------+\n|            |\n|     +------+-----+    +------+     +------+      +------+\n|     |             |    |             |            |             |\n|     | Wood 1      |    |   Screw  |            |   Wood 2  |\n|     |             |    |             |            |             |\n|     +-------------+    +------+     +------+      +------+\n|           PRESS HERE           SCREW SPINS  WOOD HOLDS \n|           WOODS TOGETHER  INTO WOOD         TIGHT!\n|            \n+------------+\n```\n\nThis is a simple picture showing how a screw helps hold two pieces of wood together by twisting and digging into them. \n\n---"
        }
    ]
    return jsonify(chat_data)

@app.route('/tasks')
def get_tasks_data():
    tasks_data = [
        {
            "tabnames": "Task One",
            "details": {
                "title": "Task One: Target information and auction process",
                "duration": "30-60 mins   Advanced",
                "bodyText": "Perform a target company deep dive and provide a summary of this auction process",
                "list": [
                    {
                        "title": "What you'll learn",
                        "list": [
                            "Meet your client WorldWide Brewing Co. who are interested in expanding their operations into Asia through M&A",
                            "How to select ideal M&A targets from strategic, financial and structural perspectives"
                        ]
                    },
                    {
                        "title": "What you'll do",
                        "list": [
                            "Email your Managing Director sharing your perspective about which M&A targets the client should explore further"
                        ]
                    }
                ]
            }
        },
        {
            "tabnames": "Task Two",
            "details": {
                "title": "Task Two: Target information and auction process",
                "duration": "30-60 mins   Advanced",
                "bodyText": "Perform a target company deep dive and provide a summary of this auction process",
                "list": [
                    {
                        "title": "What you'll learn",
                        "list": [
                            "Meet your client WorldWide Brewing Co. who are interested in expanding their operations into Asia through M&A",
                            "How to select ideal M&A targets from strategic, financial and structural perspectives"
                        ]
                    },
                    {
                        "title": "What you'll do",
                        "list": [
                            "Email your Managing Director sharing your perspective about which M&A targets the client should explore further"
                        ]
                    }
                ]
            }
        },
        {
            "tabnames": "Task Three",
            "details": {
                "title": "Task Three: Target information and auction process",
                "duration": "30-60 mins   Advanced",
                "bodyText": "Perform a target company deep dive and provide a summary of this auction process",
                "list": [
                    {
                        "title": "What you'll learn",
                        "list": [
                            "Meet your client WorldWide Brewing Co. who are interested in expanding their operations into Asia through M&A",
                            "How to select ideal M&A targets from strategic, financial and structural perspectives"
                        ]
                    },
                    {
                        "title": "What you'll do",
                        "list": [
                            "Email your Managing Director sharing your perspective about which M&A targets the client should explore further"
                        ]
                    }
                ]
            }
        },
        {
            "tabnames": "Task Four",
            "details": {
                "title": "Task Four: Target information and auction process",
                "duration": "30-60 mins   Advanced",
                "bodyText": "Perform a target company deep dive and provide a summary of this auction process",
                "list": [
                    {
                        "title": "What you'll learn",
                        "list": [
                            "Meet your client WorldWide Brewing Co. who are interested in expanding their operations into Asia through M&A",
                            "How to select ideal M&A targets from strategic, financial and structural perspectives"
                        ]
                    },
                    {
                        "title": "What you'll do",
                        "list": [
                            "Email your Managing Director sharing your perspective about which M&A targets the client should explore further"
                        ]
                    }
                ]
            }
        },
        {
            "tabnames": "Finish Line",
            "details": {
                "title": "Finish Line: Target information and auction process",
                "duration": "30-60 mins   Advanced",
                "bodyText": "Perform a target company deep dive and provide a summary of this auction process",
                "list": [
                    {
                        "title": "What you'll learn",
                        "list": [
                            "Meet your client WorldWide Brewing Co. who are interested in expanding their operations into Asia through M&A",
                            "How to select ideal M&A targets from strategic, financial and structural perspectives"
                        ]
                    },
                    {
                        "title": "What you'll do",
                        "list": [
                            "Email your Managing Director sharing your perspective about which M&A targets the client should explore further"
                        ]
                    }
                ]
            }
        }
    ]
    return jsonify(tasks_data)

@app.route('/programs')
def get_programs_data():
    programs_data = [
        {
            "name": "Intro to Programming",
            "field": "CS",
            "time": "2 - 4 hours",
            "level": "Beginner",
            "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum atque.",
            "img": "https://cdn.prod.website-files.com/5d4955a615f2c1cba8fdc3f9/623dda7e41299b3cacaacc16_HTML_Blog-scaled.jpeg"
        },
        {
            "name": "Intro to Machine Learning",
            "field": "AI",
            "time": "3 - 5 hours",
            "level": "Intermediate",
            "description": "Learn the basics of machine learning and build your first model.",
            "img": "https://atriainnovation.com/uploads/2023/11/portada-9.jpg"
        },
        {
            "name": "Digital Marketing",
            "field": "Marketing",
            "time": "4 - 6 hours",
            "level": "Beginner",
            "description": "Understand the key concepts and strategies in digital marketing.",
            "img": "https://i.ytimg.com/vi/WUniTVTi_Jk/maxresdefault.jpg"
        },
        {
            "name": "Financial Accounting",
            "field": "Finance",
            "time": "6 - 8 hours",
            "level": "Beginner",
            "description": "Gain a solid foundation in financial accounting principles and practices.",
            "img": "img.jpg"
        },
        {
            "name": "DSA",
            "field": "CS",
            "time": "5 - 7 hours",
            "level": "Intermediate",
            "description": "Master the fundamental data structures and algorithms used in computer science.",
            "img": "https://media.licdn.com/dms/image/C4D12AQEpdTFFFWiIAA/article-cover_image-shrink_600_2000/0/1581342345742?e=2147483647&v=beta&t=ihU8uxgNbJ-UxIIVDB9h-vyIvdQshmllY5PDHE8Kj-g"
        },
        {
            "name": "Graphic Design Basics",
            "field": "Design",
            "time": "2 - 3 hours",
            "level": "Beginner",
            "description": "Discover the essentials of graphic design, including tools and techniques.",
            "img": "img.jpg"
        },
        {
            "name": "Project Management",
            "field": "Business",
            "time": "5 - 7 hours",
            "level": "Intermediate",
            "description": "Learn effective project management strategies to lead successful projects.",
            "img": "img.jpg"
        }
    ]
    return jsonify(programs_data)

@app.route('/jobs')
def get_jobs_data():
    jobs_data = [
        {
            "name": "Intro to Programming",
            "field": "CS",
            "time": "2 - 4 hours",
            "level": "Beginner",
            "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum atque.",
            "img": "https://cdn.prod.website-files.com/5d4955a615f2c1cba8fdc3f9/623dda7e41299b3cacaacc16_HTML_Blog-scaled.jpeg"
        },
        {
            "name": "Intro to Machine Learning",
            "field": "AI",
            "time": "3 - 5 hours",
            "level": "Intermediate",
            "description": "Learn the basics of machine learning and build your first model.",
            "img": "https://atriainnovation.com/uploads/2023/11/portada-9.jpg"
        },
        {
            "name": "Digital Marketing",
            "field": "Marketing",
            "time": "4 - 6 hours",
            "level": "Beginner",
            "description": "Understand the key concepts and strategies in digital marketing.",
            "img": "https://i.ytimg.com/vi/WUniTVTi_Jk/maxresdefault.jpg"
        },
        {
            "name": "Financial Accounting",
            "field": "Finance",
            "time": "6 - 8 hours",
            "level": "Beginner",
            "description": "Gain a solid foundation in financial accounting principles and practices.",
            "img": "img.jpg"
        },
        {
            "name": "DSA",
            "field": "CS",
            "time": "5 - 7 hours",
            "level": "Intermediate",
            "description": "Master the fundamental data structures and algorithms used in computer science.",
            "img": "https://media.licdn.com/dms/image/C4D12AQEpdTFFFWiIAA/article-cover_image-shrink_600_2000/0/1581342345742?e=2147483647&v=beta&t=ihU8uxgNbJ-UxIIVDB9h-vyIvdQshmllY5PDHE8Kj-g"
        },
        {
            "name": "Graphic Design Basics",
            "field": "Design",
            "time": "2 - 3 hours",
            "level": "Beginner",
            "description": "Discover the essentials of graphic design, including tools and techniques.",
            "img": "img.jpg"
        },
        {
            "name": "Project Management",
            "field": "Business",
            "time": "5 - 7 hours",
            "level": "Intermediate",
            "description": "Learn effective project management strategies to lead successful projects.",
            "img": "img.jpg"
        }
    ]
    return jsonify(jobs_data)

@app.route('/signup', methods=['POST'])
def signup():
    """
    Handles user signup requests.

    Returns:
        A JSON response indicating success or failure.
    """
    data = request.get_json()

    # Basic validation (you should implement more robust validation)
    if not all(key in data for key in ['name', 'email', 'password']):
        return jsonify({"error": "Missing required fields"}), 400

    # In the real app, you would:
    # 1. Hash the password
    # 2. Check if the email is already registered
    # 3. Store the user data in a database

    # For simplicity, we'll just simulate success
    return jsonify({"message": "Signup successful"}), 201



if __name__ == '__main__':
    app.run(debug=True)
