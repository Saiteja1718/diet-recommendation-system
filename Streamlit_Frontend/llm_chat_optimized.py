"""
Enhanced intelligent chat system with context-aware responses.
"""

import streamlit as st
import re

# Comprehensive FAQ responses
FAQ_RESPONSES = {
    "substitute": """Here are common ingredient substitutions:
    
🥚 **Eggs**: Use flax eggs (1 tbsp ground flaxseed + 3 tbsp water per egg), applesauce, or mashed banana
🥛 **Milk**: Try almond milk, oat milk, soy milk, or coconut milk
🧈 **Butter**: Use coconut oil, olive oil, or vegan butter
🍖 **Chicken**: Substitute with tofu, tempeh, or chickpeas
🐟 **Fish**: Try tofu, mushrooms, or plant-based alternatives
🧀 **Cheese**: Use nutritional yeast, cashew cheese, or vegan cheese
🍞 **Bread**: Try lettuce wraps, rice paper, or gluten-free bread
🍝 **Pasta**: Use zucchini noodles, shirataki noodles, or whole wheat pasta""",
    
    "allergy": """For common allergies, here are safe alternatives:

🥜 **Nut Allergies**: Use sunflower seed butter, tahini, or soy nut butter
🌾 **Gluten**: Choose rice, quinoa, buckwheat, or certified gluten-free products
🥛 **Dairy**: Opt for coconut, almond, oat, or soy-based alternatives
🦐 **Shellfish**: Avoid all shellfish; use plant-based proteins instead
🥚 **Eggs**: Use commercial egg replacers or flax/chia eggs

Always read labels carefully and consult with a healthcare provider for severe allergies.""",
    
    "cooking": """Quick cooking tips:

⏱️ **Save Time**: Prep ingredients in advance, use a pressure cooker, or batch cook
🔥 **Better Flavor**: Season in layers, taste as you go, and let meat rest before cutting
🥘 **Texture**: Don't overcrowd the pan, use high heat for searing, low for braising
❄️ **Storage**: Cool food before refrigerating, use airtight containers, label with dates
♻️ **Reduce Waste**: Save vegetable scraps for stock, freeze herbs in oil, repurpose leftovers""",
    
    "nutrition": """Nutrition basics:

🥗 **Balanced Plate**: 1/2 vegetables, 1/4 protein, 1/4 whole grains
💪 **Protein**: Aim for 0.8g per kg body weight (more if active)
🥤 **Hydration**: Drink 8-10 glasses of water daily
🍎 **Fiber**: Get 25-30g daily from fruits, vegetables, and whole grains
🥑 **Healthy Fats**: Include nuts, seeds, avocado, and olive oil
🍬 **Sugar**: Limit added sugars to less than 10% of daily calories""",
    
    "meal_prep": """Meal prep strategies:

📅 **Plan Ahead**: Choose 3-4 recipes for the week
🛒 **Smart Shopping**: Make a list, shop once, buy in bulk
🍱 **Batch Cook**: Cook grains, proteins, and veggies in large batches
📦 **Portion Control**: Use containers to pre-portion meals
❄️ **Freeze Smart**: Label everything, freeze flat for easy storage
🔄 **Mix & Match**: Prepare versatile ingredients that work in multiple dishes""",
    
    "budget": """Eating healthy on a budget:

💰 **Buy Smart**: Choose seasonal produce, buy frozen vegetables, use store brands
🌾 **Protein Sources**: Eggs, beans, lentils, and canned fish are affordable
🥫 **Pantry Staples**: Stock rice, pasta, canned tomatoes, and dried beans
🥬 **Reduce Waste**: Use leftovers creatively, freeze extras, plan portions
🛍️ **Shop Sales**: Buy in bulk when on sale, use coupons, compare unit prices"""
}

def extract_recipe_info_from_context(context_text):
    """Extract recipe names and details from context for intelligent responses."""
    recipes = []
    try:
        lines = context_text.split('\n')
        current_recipe = {}
        
        for line in lines:
            if 'Name:' in line or 'Recipe:' in line:
                if current_recipe:
                    recipes.append(current_recipe)
                current_recipe = {'name': line.split(':', 1)[1].strip() if ':' in line else line}
            elif 'Calories:' in line and current_recipe:
                try:
                    cal_match = re.search(r'(\d+\.?\d*)', line)
                    if cal_match:
                        current_recipe['calories'] = float(cal_match.group(1))
                except:
                    pass
            elif 'Protein' in line and current_recipe:
                try:
                    prot_match = re.search(r'(\d+\.?\d*)', line)
                    if prot_match:
                        current_recipe['protein'] = float(prot_match.group(1))
                except:
                    pass
                    
        if current_recipe:
            recipes.append(current_recipe)
    except:
        pass
    
    return recipes

def get_intelligent_response(user_question: str, context_text: str) -> str:
    """
    Provide intelligent, context-aware responses based on the question and available recipe data.
    """
    question_lower = user_question.lower()
    recipes = extract_recipe_info_from_context(context_text)
    
    # Question about specific recipes
    if any(word in question_lower for word in ['recipe', 'meal', 'dish', 'food']):
        if recipes:
            recipe_list = "\n".join([f"• **{r.get('name', 'Unknown')}**" + 
                                    (f" ({r.get('calories', 0):.0f} cal)" if 'calories' in r else "")
                                    for r in recipes[:5]])
            return f"""Based on your recommendations, here are your recipes:

{recipe_list}

Each recipe is tailored to your nutritional needs. Would you like to know more about a specific recipe, or need help with substitutions?"""
        else:
            return "I don't see any recipes in your current recommendations. Please generate some recommendations first, then I can help you with specific questions about them!"
    
    # Questions about calories/nutrition
    if any(word in question_lower for word in ['calorie', 'calories', 'nutrition', 'protein', 'carb', 'fat']):
        if recipes and any('calories' in r for r in recipes):
            total_cal = sum(r.get('calories', 0) for r in recipes)
            avg_cal = total_cal / len(recipes) if recipes else 0
            high_protein = len([r for r in recipes if r.get('protein', 0) > 20])
            return f"""Nutritional Overview:

• Total Calories: {total_cal:.0f} kcal across {len(recipes)} recipes
• Average per Recipe: {avg_cal:.0f} kcal
• Protein-rich options: {high_protein} recipes with 20g+ protein

{FAQ_RESPONSES['nutrition']}

Need help adjusting your calorie intake or finding higher/lower calorie options?"""
        else:
            return FAQ_RESPONSES['nutrition']
    
    # Questions about substitutions
    if any(word in question_lower for word in ['substitute', 'replace', 'instead', 'swap', 'alternative', 'change']):
        ingredients = ['egg', 'milk', 'butter', 'chicken', 'fish', 'cheese', 'bread', 'pasta']
        mentioned = [ing for ing in ingredients if ing in question_lower]
        
        if mentioned:
            response = f"Great question about substituting **{mentioned[0]}**!\n\n"
            response += FAQ_RESPONSES['substitute']
            if recipes:
                response += f"\n\nTip: You have {len(recipes)} recipes. I can help you modify any of them with these substitutions!"
            return response
        return FAQ_RESPONSES['substitute']
    
    # Questions about allergies
    if any(word in question_lower for word in ['allergy', 'allergic', 'intolerance', 'sensitive', 'avoid']):
        return FAQ_RESPONSES['allergy']
    
    # Questions about cooking
    if any(word in question_lower for word in ['cook', 'prepare', 'make', 'how to', 'tips', 'bake', 'fry', 'boil']):
        return FAQ_RESPONSES['cooking']
    
    # Questions about meal prep
    if any(word in question_lower for word in ['meal prep', 'prepare ahead', 'batch', 'planning', 'week', 'advance']):
        return FAQ_RESPONSES['meal_prep']
    
    # Questions about budget
    if any(word in question_lower for word in ['budget', 'cheap', 'affordable', 'save money', 'cost', 'price', 'expensive']):
        if recipes:
            return f"""Budget-Friendly Tips for Your {len(recipes)} Recipes:

{FAQ_RESPONSES['budget']}

Pro Tip: Buy ingredients that appear in multiple recipes to save money and reduce waste!"""
        return FAQ_RESPONSES['budget']
    
    # Questions about specific days/meals (for meal planner)
    if any(word in question_lower for word in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'breakfast', 'lunch', 'dinner', 'snack']):
        if 'swap' in question_lower or 'change' in question_lower or 'different' in question_lower:
            return """Swapping Meals:

You can easily modify your meal plan:

1. Same Nutrition: Look for recipes with similar calorie counts
2. Keep Variety: Try different cuisines with the same nutritional profile
3. Batch Cooking: Swap to recipes that share ingredients for efficiency

Would you like suggestions for alternative recipes with similar nutrition?"""
        elif context_text and ('meal plan' in context_text.lower() or 'weekly' in context_text.lower()):
            return """About Your Meal Plan:

Your plan is customized for your goals. Each meal is balanced for:
• Calorie targets
• Protein requirements
• Nutritional variety

Need to adjust a specific day or meal? Just let me know which one!"""
    
    # General help
    if any(word in question_lower for word in ['help', 'what can', 'how do', '?']):
        topic_count = len(recipes) if recipes else "your"
        return f"""I'm here to help with {topic_count} recipes!

I can assist you with:

• Ingredient Substitutions - Swap ingredients you don't have
• Allergy Alternatives - Safe alternatives for common allergens
• Cooking Tips - Techniques and time-saving tricks
• Nutrition Advice - Understanding your nutritional needs
• Meal Prep - Planning and preparing meals efficiently
• Budget Tips - Eating healthy affordably
• Recipe Questions - Details about your recommended recipes

Just ask me anything! For example:
- "How can I substitute eggs?"
- "What are the calories in my recipes?"
- "How do I meal prep for the week?"
"""
    
    # Default response with context
    if recipes:
        return f"""I have information about your {len(recipes)} recommended recipes!

I can help you with:
• Ingredient substitutions
• Nutritional information
• Cooking tips and techniques
• Meal prep strategies
• Budget-friendly alternatives

Try asking:
- "What are the calories in these recipes?"
- "How can I substitute [ingredient]?"
- "Give me cooking tips"
- "How do I meal prep these?"

What would you like to know?"""
    else:
        return """I'm your diet assistant! I can help with:
        
• Ingredient substitutions - Ask about swapping ingredients
• Allergy alternatives - Get safe food alternatives  
• Cooking tips - Learn cooking techniques
• Nutrition advice - Understand nutritional basics
• Meal prep - Plan and prepare meals efficiently
• Budget tips - Eat healthy affordably

Ask me anything about diet, nutrition, or cooking!"""


def generate_chat_answer(context_text: str, history_text: str, user_message: str, use_ai: bool = False) -> str:
    """
    Generate a chat response. Uses intelligent FAQ by default, or LLM if enabled.
    
    Args:
        context_text: Text describing current recommended recipes
        history_text: Previous chat history
        user_message: The user's question
        use_ai: If True, use LLM (slow). If False, use intelligent FAQ responses.
        
    Returns:
        The assistant's reply
    """
    if not use_ai:
        # Intelligent context-aware response
        return get_intelligent_response(user_message, context_text)
    
    # LLM-based response (slow but more personalized)
    try:
        # Import here to avoid loading if not needed
        from llm_chat import generate_chat_answer as llm_generate
        return llm_generate(context_text, history_text, user_message)
    except Exception as e:
        return f"AI chat error: {str(e)}. Using Quick Response mode instead.\n\n" + get_intelligent_response(user_message, context_text)
