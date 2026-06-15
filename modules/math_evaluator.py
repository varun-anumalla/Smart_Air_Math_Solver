class MathEvaluator:

    def solve(self, expression):

        try:

            expression = expression.replace(
                " ",
                ""
            )

            answer = eval(
                expression
            )

            return str(
                answer
            )

        except:

            return "Invalid Expression"